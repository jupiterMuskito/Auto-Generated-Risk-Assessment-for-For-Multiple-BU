"""Where each business unit's active register comes from, and how admins replace it.

Lookup order for a business unit:
  1. Uploaded register  - data/registers/<bu_id>.xlsx   (activated on the Register admin tab)
  2. Built-in default   - the file named in bu_config.json "register" (in the repo's registers/ folder)
  3. Built-in default   - regenerated from ra/defaults/<bu_id>.py if that file is missing (refinery and fertiliser only)
  4. None               - "Risk register update required" report

Streamlit Community Cloud wipes uploaded files when the app restarts. To make an upload permanent, either add a [github]
section to Secrets (the app then commits the file to the repo for you) or download it and commit it to registers/ yourself.
"""
from __future__ import annotations

import base64
import json
import shutil
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path

import streamlit as st

from .engine import Register, RegisterError, load_register

ROOT = Path(__file__).resolve().parent.parent
REG_DIR = ROOT / "registers"
UPLOAD_DIR = ROOT / "data" / "registers"
HISTORY_DIR = UPLOAD_DIR / "history"
GEN_DIR = UPLOAD_DIR / "_builtin"
TMP_DIR = UPLOAD_DIR / "_tmp"


@st.cache_resource(show_spinner=False)
def _load(path: str, mtime: float) -> Register:
    return load_register(path)


def _bundled_path(bu: dict) -> Path | None:
    if not bu.get("register"):
        return None
    p = ROOT / bu["register"]
    if p.exists():
        return p
    alt = ROOT / Path(bu["register"]).name          # tolerate the file having been uploaded to the repo root
    return alt if alt.exists() else p


def _builtin_source(bu: dict) -> str | None:
    src = bu.get("default_source")
    return src if src and (ROOT / "ra" / "defaults" / f"{src}.py").exists() else None


def upload_path(bu: dict) -> Path:
    return UPLOAD_DIR / f"{bu['id']}.xlsx"


def meta_path(bu: dict) -> Path:
    return UPLOAD_DIR / f"{bu['id']}.json"


def read_meta(bu: dict) -> dict:
    try:
        return json.loads(meta_path(bu).read_text(encoding="utf-8"))
    except Exception:
        return {}


def default_path(bu: dict) -> Path | None:
    """Built-in default file for the BU (bundled, or regenerated from its own source module)."""
    p = _bundled_path(bu)
    if p and p.exists():
        return p
    src = _builtin_source(bu)
    if not src:
        return None
    from .defaults.build import build
    out = GEN_DIR / (Path(bu["register"]).name if bu.get("register") else f"{bu['id']}_default.xlsx")
    if not out.exists():
        build(src, out)
    return out


def resolve(bu: dict) -> tuple[Register | None, str, str | None]:
    """Returns (register, source label, problem). Falls back to the default if an uploaded file is unreadable."""
    problems = []
    up = upload_path(bu)
    if up.exists():
        try:
            return _load(str(up), up.stat().st_mtime), "Uploaded", None
        except RegisterError as exc:
            problems.append(f"Uploaded register could not be used ({exc}); using the built-in default.")
    try:
        dp = default_path(bu)
    except Exception as exc:  # builder failure
        dp, _ = None, problems.append(f"Built-in default could not be created ({exc}).")
    if dp is None or not dp.exists():
        why = ("No risk register has been linked to this business unit yet." if not bu.get("register") and not _builtin_source(bu)
               else f"The register file '{Path(bu.get('register') or '').name}' has not been uploaded yet.")
        return None, "", " ".join(problems + [why])
    try:
        label = "Built-in default" if dp.parent != GEN_DIR else "Built-in default (regenerated)"
        return _load(str(dp), dp.stat().st_mtime), label, " ".join(problems) or None
    except RegisterError as exc:
        return None, "", " ".join(problems + [f"The register could not be used: {exc}"])


def activate(bu: dict, data: bytes, user: str, note: str, fingerprint: str) -> Path:
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    hist = HISTORY_DIR / bu["id"]
    hist.mkdir(parents=True, exist_ok=True)
    (hist / f"{stamp}_{fingerprint}.xlsx").write_bytes(data)
    tmp = upload_path(bu).with_suffix(".tmp")
    tmp.write_bytes(data)
    tmp.replace(upload_path(bu))
    meta_path(bu).write_text(json.dumps({"uploaded_by": user, "uploaded_at": datetime.now().isoformat(timespec="seconds"),
                                         "fingerprint": fingerprint, "note": note}, indent=1), encoding="utf-8")
    return upload_path(bu)


def revert_to_default(bu: dict):
    for p in (upload_path(bu), meta_path(bu)):
        if p.exists():
            p.unlink()


def history(bu: dict) -> list[Path]:
    d = HISTORY_DIR / bu["id"]
    return sorted(d.glob("*.xlsx"), reverse=True) if d.exists() else []


# ----------------------------------------------------------------------------- optional GitHub persistence
def github_cfg() -> dict:
    try:
        g = dict(st.secrets.get("github", {}))
    except Exception:
        return {}
    return g if g.get("token") and g.get("repo") else {}


def github_commit(bu: dict, data: bytes, user: str, note: str) -> str:
    """Commits the workbook to the repo at the BU's register path so it survives restarts and becomes the new default."""
    g = github_cfg()
    if not g:
        raise RuntimeError("GitHub is not configured in Secrets.")
    path = (bu.get("register") or f"registers/{bu['id'].upper()}_Register.xlsx").replace("\\", "/")
    branch = g.get("branch", "main")
    url = f"https://api.github.com/repos/{g['repo']}/contents/{path}"
    hdr = {"Authorization": f"Bearer {g['token']}", "Accept": "application/vnd.github+json", "User-Agent": "ra-generator"}
    sha = None
    try:
        with urllib.request.urlopen(urllib.request.Request(f"{url}?ref={branch}", headers=hdr), timeout=20) as r:
            sha = json.loads(r.read())["sha"]
    except urllib.error.HTTPError as e:
        if e.code != 404:
            raise RuntimeError(f"GitHub read failed ({e.code}).") from e
    body = {"message": f"Register update: {bu['name']} by {user}" + (f" - {note}" if note else ""),
            "content": base64.b64encode(data).decode(), "branch": branch}
    if sha:
        body["sha"] = sha
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers={**hdr, "Content-Type": "application/json"}, method="PUT")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read())["commit"]["html_url"]
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"GitHub commit failed ({e.code}). Check the token has 'Contents: read and write' on {g['repo']}.") from e


def clear_tmp():
    shutil.rmtree(TMP_DIR, ignore_errors=True)
