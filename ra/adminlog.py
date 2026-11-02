"""Admin password and assessment log - ported from the Admin page of the original OKPELLA HTML app.

Admin password: PBKDF2-SHA256 hash. Order of precedence (same idea as the HTML app's device override):
  1. a password changed on the Admin page  -> data/admin_cred.json
  2. [admin] password_hash in Secrets
  3. the built-in credential (default password below - change it on first use)
Assessment log: newest first, capped at 1000 entries (as in the HTML app), one entry per generated assessment;
exportedAt is filled in when the PDF is downloaded.
"""
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

import streamlit as st

from .auth import hash_password, verify

ROOT = Path(__file__).resolve().parent.parent
CRED_FILE = ROOT / "data" / "admin_cred.json"
LOG_FILE = ROOT / "data" / "assessment_log.json"
LOG_CAP = 1000
DEFAULT_ADMIN_PASSWORD = "OkpellaAdmin@2026"
_BUILTIN = None

LOG_COLS = ["serial", "generatedAt", "businessUnit", "registerFingerprint", "jobType", "equipmentType", "equipmentRef", "equipmentMotion",
            "equipmentStatus", "location", "workArea", "department", "generationMethod", "activityCount", "hazardCount", "hazardsIncluded",
            "hazardsExcluded", "exportedAt", "extreme", "high", "moderate", "low", "negligible", "assessedBy", "approvedBy", "activities"]


# ----------------------------------------------------------------------------- admin password
def _builtin_hash() -> str:
    global _BUILTIN
    if _BUILTIN is None:
        _BUILTIN = hash_password(DEFAULT_ADMIN_PASSWORD, "6f6b70656c6c612d61646d696e2d3236")
    return _BUILTIN


def cred_source() -> str:
    if CRED_FILE.exists():
        return "changed on the Admin page"
    try:
        if st.secrets.get("admin", {}).get("password_hash"):
            return "Secrets"
    except Exception:
        pass
    return "built-in default"


def current_hash() -> str:
    try:
        return json.loads(CRED_FILE.read_text(encoding="utf-8"))["hash"]
    except Exception:
        pass
    try:
        h = st.secrets.get("admin", {}).get("password_hash")
        if h:
            return h
    except Exception:
        pass
    return _builtin_hash()


def verify_admin(pw: str) -> bool:
    return bool(pw) and verify(pw, current_hash())


def change_admin(new_pw: str, user: str):
    CRED_FILE.parent.mkdir(parents=True, exist_ok=True)
    CRED_FILE.write_text(json.dumps({"hash": hash_password(new_pw), "changedBy": user,
                                     "changedAt": datetime.now().isoformat(timespec="seconds")}), encoding="utf-8")


# ----------------------------------------------------------------------------- assessment log
def read_log() -> list[dict]:
    try:
        return json.loads(LOG_FILE.read_text(encoding="utf-8"))
    except Exception:
        return []


def write_log(a: list[dict]):
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    tmp = LOG_FILE.with_suffix(".tmp")
    tmp.write_text(json.dumps(a, ensure_ascii=False), encoding="utf-8")
    tmp.replace(LOG_FILE)


def append_log(entry: dict):
    a = read_log()
    a.insert(0, entry)
    write_log(a[:LOG_CAP])


def mark_exported(serial: str, when: str, included: int, excluded: int):
    a = read_log()
    for x in a:
        if x.get("serial") == serial:
            x["exportedAt"], x["hazardsIncluded"], x["hazardsExcluded"] = when, included, excluded
            break
    write_log(a)


def log_csv(rows: list[dict]) -> bytes:
    def q(v):
        if isinstance(v, list):
            v = "; ".join(map(str, v))
        v = "" if v is None else str(v)
        return '"' + v.replace('"', '""') + '"'
    body = ",".join(LOG_COLS) + "\r\n" + "\r\n".join(",".join(q(r.get(c)) for c in LOG_COLS) for r in rows)
    return ("\ufeff" + body).encode("utf-8")
