"""Risk Assessment Generator - Streamlit, multi-business-unit (v5).

Flow: sign in -> select business unit -> (register available) build job -> identify hazards -> review/untick -> PDF
                                       -> (no register)        register-update-required report
"""
from __future__ import annotations

import csv
import html
import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import sys

import pandas as pd
import streamlit as st

sys.path.insert(0, str(Path(__file__).parent))
from ra import auth, theme
from ra.engine import (CATS, LEVEL_NAME, OTHER_LOC_NAME, RegisterError, blank_template_bytes, collect_hazards, compile_ppe,
                       counts, load_register, make_serial, suggest_from_text)
from ra.pdf_report import build_pdf, build_register_request_pdf

ROOT = Path(__file__).parent
LOG = ROOT / "data" / "assessment_log.csv"
TZ = ZoneInfo("Africa/Lagos")
OTHER = "__other__"
st.set_page_config(page_title="Risk Assessment Generator", page_icon="🦺", layout="centered")
theme.apply()
ss = st.session_state


# ============================================================================ helpers
def load_bus() -> list[dict]:
    return json.loads((ROOT / "bu_config.json").read_text(encoding="utf-8"))["business_units"]


@st.cache_resource(show_spinner=False)
def _load(path: str, mtime: float):
    return load_register(path)


def bu_register(bu: dict):
    """Returns (Register, None) or (None, reason)."""
    if not bu.get("register"):
        return None, "No risk register has been linked to this business unit yet."
    p = ROOT / bu["register"]
    if not p.exists():
        return None, f"The register file '{p.name}' was not found in the app's registers folder."
    try:
        return _load(str(p), p.stat().st_mtime), None
    except RegisterError as exc:
        return None, f"The register could not be used: {exc}"


def esc(x) -> str:
    return html.escape(str(x or ""))


def now() -> datetime:
    return datetime.now(TZ)


def log_event(row: dict):
    LOG.parent.mkdir(exist_ok=True)
    cols = ["event", "time", "user", "bu", "serial", "jobType", "description", "department", "location", "workArea", "equipmentType",
            "equipmentRef", "motion", "status", "method", "activities", "activityCount", "hazardCount", "hazardsIncluded",
            "hazardsExcluded", "extreme", "high", "moderate", "low", "negligible", "assessedBy", "approvedBy", "registerFingerprint", "note"]
    new = not LOG.exists()
    with LOG.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        if new:
            w.writeheader()
        w.writerow({c: row.get(c, "") for c in cols})


FIELDS = ["f_jt", "f_desc", "f_dept", "f_by", "f_rev", "f_loc", "f_loc_other", "f_et", "f_et_other", "f_eq", "f_eq_other",
          "f_area", "f_mo", "f_st", "f_tags"]


def reset_job():
    for k in list(ss.keys()):
        if k in FIELDS or k.startswith("inc_") or k in ("result", "started", "methods", "suggest_msg", "val_msg", "preset_q"):
            del ss[k]


def set_bu(bu_id: str | None):
    reset_job()
    ss.pop("bu_pick", None)
    if bu_id:
        ss["bu_id"] = bu_id
    else:
        ss.pop("bu_id", None)


# ============================================================================ sign-in
user = auth.require_sign_in(lambda: theme.appbar())
BUS = load_bus()
BU_BY_ID = {b["id"]: b for b in BUS}

# ============================================================================ sidebar
with st.sidebar:
    st.markdown(f"**Signed in:** {esc(user.get('name') or user.get('username'))}")
    if auth.test_account_active() and user.get("username") == auth.TEST_USER:
        st.warning("Test account in use - add real users in Secrets before live use.")
    def _sign_out():
        auth.sign_out()
        set_bu(None)
    st.button("Sign out", width="stretch", on_click=_sign_out)
    if ss.get("bu_id"):
        st.divider()
        st.markdown(f"**Business unit:** {esc(BU_BY_ID[ss['bu_id']]['name'])}")
        st.button("Change business unit", width="stretch", on_click=set_bu, args=(None,))

# ============================================================================ step 0: business unit
if not ss.get("bu_id") or ss["bu_id"] not in BU_BY_ID:
    theme.appbar()
    with st.container(border=True):
        st.markdown("### Select business unit")
        st.markdown('<p class="hint">Hazards are taken only from the selected business unit\'s risk register.</p>', unsafe_allow_html=True)
        status = {b["id"]: bu_register(b) for b in BUS}
        label = lambda i: BU_BY_ID[i]["name"] + ("" if status[i][0] else "  (no register)")
        choice = st.selectbox("Business unit", [b["id"] for b in BUS], format_func=label, index=None, key="bu_pick", placeholder="— select business unit —")
        for b in BUS:
            reg, why = status[b["id"]]
            state = (f'<span class="ok">Register loaded</span> · {len(reg.activity_hazards) + len(reg.equipment_hazards)} hazards · '
                     f'fingerprint {reg.fingerprint}') if reg else f'<span class="bad">No usable register</span> · {esc(why)}'
            st.markdown(f'<div class="bu-card"><div class="n">{esc(b["name"])}</div><div class="d">{state}</div></div>', unsafe_allow_html=True)
        st.button("Continue", type="primary", width="stretch", disabled=choice is None, on_click=set_bu, args=(choice,))
    st.stop()

BU = BU_BY_ID[ss["bu_id"]]
R, why_not = bu_register(BU)
settings = R.settings if R else {}
COMPANY = settings.get("CompanyName") or BU.get("company") or BU["name"].upper()
ERP = [settings[k] for k in ("ERP1", "ERP2", "ERP3", "ERP4") if settings.get(k)] or BU.get("erp") or \
      ["Emergency contact numbers for this business unit have not been set - add ERP lines to the register's Settings sheet."]
theme.appbar(BU["name"])

# ============================================================================ no register -> update-required report
if R is None:
    st.markdown(f'<div class="noreg"><h4>Risk register update required</h4>'
                f'Risk assessments cannot be generated for <b>{esc(BU["name"])}</b>. {esc(why_not)}<br>'
                f'Every hazard in an assessment must come from the business unit\'s approved register, so the register owner '
                f'(<b>{esc(BU.get("register_owner", "BU HSE"))}</b>) needs to upload or update it.</div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown("### Register update request")
        c1, c2 = st.columns(2)
        req_by = c1.text_input("Requested by", value=user.get("name", ""))
        req_dept = c2.text_input("Department / section")
        req_note = st.text_area("Work you need to assess (optional)", placeholder="e.g. Boiler tube inspection at the sugar refinery boiler house")
        when = now().strftime("%d %b %Y %H:%M")
        req = {"bu": BU["name"], "when": when, "rows": [
            ("Business unit", BU["name"]), ("Register owner", BU.get("register_owner", "")), ("Register status", why_not),
            ("Requested by", req_by or "-"), ("Department / section", req_dept or "-"), ("Work to be assessed", req_note or "-"),
            ("Date of request", when)]}
        st.download_button("Download update request (PDF)", data=build_register_request_pdf(req),
                           file_name=f"Register_Update_Request_{BU['id']}_{now():%Y%m%d}.pdf", mime="application/pdf",
                           type="primary", width="stretch",
                           on_click=lambda: log_event({"event": "register_request", "time": now().isoformat(), "user": user.get("username"),
                                                       "bu": BU["name"], "note": f"{req_by} / {req_dept} / {req_note}"}))
        st.download_button("Download blank register template (.xlsx)", data=blank_template_bytes(),
                           file_name=f"{BU['id'].upper()}_Risk_Register_TEMPLATE.xlsx",
                           mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", width="stretch")
        st.caption("Send the request and template to the register owner. Once the approved workbook is placed in the app's "
                   "registers folder and linked in bu_config.json, this business unit will generate assessments like the others.")
    st.stop()

# ============================================================================ register available
if R.warnings:
    with st.sidebar.expander(f"Register check: {len(R.warnings)} issue(s)"):
        for w in R.warnings[:60]:
            st.caption(w)
st.sidebar.caption(f"Register fingerprint **{R.fingerprint}** · {len(R.activity_hazards)} activity + {len(R.equipment_hazards)} "
                   f"equipment hazards · {len(R.job_tags)} activities")
if settings.get("RegisterStatus"):
    st.sidebar.info(f"Register status: {settings['RegisterStatus']}")

TAGCAT = {t["t"]: t["c"] for t in R.job_tags}
LOC_ORDER = {"Process": 0, "Utility": 1, "Site": 2, "Building": 3, "Other": 4}
LOCS = [l["n"] for l in sorted(R.locations, key=lambda l: LOC_ORDER.get(l["type"], 5)) if l["n"] != OTHER_LOC_NAME]
ss.setdefault("methods", set())


def apply_preset(p):
    reset_job()
    ss.update(f_jt=p["n"], f_desc=p["d"], f_tags=[t for t in p["tags"] if t in TAGCAT], f_loc=p["loc"] if p["loc"] in LOCS else "",
              f_et=p["et"] if p["et"] in R.equipment_types else "", f_eq=p["ref"] if R.equip(p["ref"]) else "",
              f_mo=p["mo"] if p["mo"] in ("Running", "Static") else "Static",
              f_st=p["st"] if p["st"] in ("Operational", "Shutdown/Isolated") else "Operational",
              f_by=user.get("name", ""), started=True, methods={"Preset"})


def start_scratch():
    reset_job()
    ss.update(started=True, methods={"From scratch"}, f_by=user.get("name", ""))


def on_type_change():
    eq = R.equip(ss.get("f_eq", ""))
    if eq and eq["t"] != ss.get("f_et"):
        ss["f_eq"] = ""


def on_equip_change():
    eq = R.equip(ss.get("f_eq", ""))
    if eq and ss.get("f_et") != eq["t"]:
        ss["f_et"] = eq["t"]       # keep header and hazards consistent with the chosen item


def do_suggest():
    s = suggest_from_text(R, f"{ss.get('f_jt', '')}. {ss.get('f_desc', '')}")
    before = set(ss.get("f_tags", []))
    ss["f_tags"] = list(before | set(s["tags"]))
    added = [t for t in s["tags"] if t not in before]
    msg = []
    if added:
        msg.append("Added: " + "; ".join(f"**{t}** ({s['reasons'][t]})" for t in added))
    if s["equipment"] and not ss.get("f_eq"):
        ss["f_eq"], ss["f_et"] = s["equipment"], s["equipment_type"]
        msg.append(f"Equipment set to **{s['equipment']}**")
    if s["motion"]:
        ss["f_mo"], ss["f_st"] = s["motion"], s["status"]
        msg.append(f"Motion/status set to **{s['motion']} / {s['status']}**")
    ss["suggest_msg"] = "  \n".join(msg) if msg else "Nothing new recognised - add activities from the list below."
    ss["methods"].add("Description assist")


tab_build, tab_reg = st.tabs(["Build", "Register"])

# ============================================================================ BUILD
def render_build():
    if not ss.get("started"):
        with st.container(border=True):
            st.markdown("### Start from a common task")
            st.markdown('<p class="hint">Tap a job you\'re about to do. It fills in the activities and equipment for you — '
                        'you can adjust everything afterwards.</p>', unsafe_allow_html=True)
            q = st.text_input("Search tasks", key="preset_q", placeholder="Search tasks…", label_visibility="collapsed").lower().strip()
            plist = [p for p in R.presets if not q or q in f"{p['n']} {p['d']} {p['cat']} {' '.join(p['tags'])}".lower()]
            if not R.presets:
                st.caption("This register has no task presets.")
            elif not plist:
                st.caption("No matching tasks — try “start from scratch” below.")
            for cat in dict.fromkeys(p["cat"] for p in plist):
                with st.expander(f"{cat}  ·  {sum(p['cat'] == cat for p in plist)}", expanded=bool(q)):
                    for p in [x for x in plist if x["cat"] == cat]:
                        st.markdown(f"**{esc(p['n'])}**  \n<span class='hint'>{esc(p['d'])} · {len(p['tags'])} activities · "
                                    f"{esc(p['loc'] or 'choose area')}</span>", unsafe_allow_html=True)
                        st.button("Use this task", key=f"pre_{p['id']}_{p['n']}", on_click=apply_preset, args=(p,))
            st.button("Start from scratch", width="stretch", on_click=start_scratch)
        return

    # ---------------- 1. Job details
    with st.container(border=True):
        st.markdown("### 1 · Job details")
        st.text_input("Job title *", key="f_jt", placeholder="e.g. Pump seal replacement")
        st.text_area("Description *", key="f_desc", placeholder="Task, tools and method — e.g. Replace mechanical seal on the reflux pump using spanners and chain block after isolation")
        st.button("Suggest activities from description", on_click=do_suggest)
        if ss.get("suggest_msg"):
            st.info(ss["suggest_msg"])
        st.text_input("Department / Section *", key="f_dept", placeholder="e.g. Mechanical Maintenance")
        c1, c2 = st.columns(2)
        c1.text_input("Assessed by *", key="f_by")
        c2.text_input("Reviewed / Approved by *", key="f_rev")

    # ---------------- 2. Location & equipment
    with st.container(border=True):
        st.markdown("### 2 · Location & equipment")
        st.markdown('<p class="hint">Choose the area first — the equipment lists narrow to what is found there.</p>', unsafe_allow_html=True)
        loc_opts = [""] + LOCS + [OTHER]
        if ss.get("f_loc") not in loc_opts:
            ss["f_loc"] = ""
        st.selectbox("Location of work *", loc_opts, key="f_loc",
                     format_func=lambda v: "— select area —" if v == "" else "Other area (specify)…" if v == OTHER else f"{v}  ·  {R.loc_type(v)}")
        if ss["f_loc"] == OTHER:
            st.text_input("Specify the area *", key="f_loc_other")
        loc = ss["f_loc"] if ss["f_loc"] not in ("", OTHER) else ""
        here_types = {e["t"] for e in R.equipment if R.available(e, loc)}
        types_sorted = sorted(R.equipment_types, key=lambda t: (t not in here_types, R.equipment_types.index(t))) if loc else R.equipment_types
        et_opts = [""] + types_sorted + [OTHER]
        if ss.get("f_et") not in et_opts:
            ss["f_et"] = ""
        st.selectbox("Equipment type *", et_opts, key="f_et", on_change=on_type_change,
                     format_func=lambda v: "— select equipment type —" if v == "" else "Other type (specify)…" if v == OTHER
                     else (v if not loc or v in here_types else f"{v}  (not listed in this area)"))
        if ss["f_et"] == OTHER:
            st.text_input("Describe the equipment type *", key="f_et_other")
            st.caption("An unlisted equipment type has no equipment-specific hazards in the register, so only activity hazards will be generated.")
        et = ss["f_et"]
        of_type = [e for e in R.equipment if not et or et == OTHER or e["t"] == et]
        here = [e["n"] for e in of_type if R.available(e, loc)]
        elsewhere = [e["n"] for e in of_type if not R.available(e, loc)]
        eq_opts = [""] + here + elsewhere + [OTHER]
        if ss.get("f_eq") not in eq_opts:
            ss["f_eq"] = ""
        st.selectbox("Specific equipment *", eq_opts, key="f_eq", on_change=on_equip_change,
                     format_func=lambda v: "— select equipment —" if v == "" else "Other equipment (specify)…" if v == OTHER
                     else (f"{v}  (other area)" if v in elsewhere else v))
        if ss["f_eq"] == OTHER:
            st.text_input("Name the equipment (e.g. tag number) *", key="f_eq_other")
        st.text_input("Specific work area *", key="f_area", placeholder="e.g. pump row, ground level, north side")
        c1, c2 = st.columns(2)
        ss.setdefault("f_mo", "Running")
        ss.setdefault("f_st", "Operational")
        c1.selectbox("Motion", ["Running", "Static"], key="f_mo")
        c2.selectbox("Status", ["Operational", "Shutdown/Isolated"], key="f_st")

    # ---------------- 3. Activities
    with st.container(border=True):
        sel = [t for t in ss.get("f_tags", []) if t in TAGCAT]
        ss["f_tags"] = sel
        st.markdown(f"### 3 · Activities · {len(sel)}")
        st.markdown('<p class="hint">Type to search all activities. The register links each activity to its hazards.</p>', unsafe_allow_html=True)
        st.multiselect("Activities", R.tag_names, key="f_tags", format_func=lambda t: f"{t}  ·  {TAGCAT.get(t, '')}",
                       placeholder="Search activities…", label_visibility="collapsed")

    # ---------------- resolve + validate
    def val(k, other):
        v = ss.get(k, "")
        return (ss.get(other, "") or "").strip() if v == OTHER else v

    J = dict(jt=ss.get("f_jt", "").strip(), desc=ss.get("f_desc", "").strip(), dept=ss.get("f_dept", "").strip(),
             by=ss.get("f_by", "").strip(), rev=ss.get("f_rev", "").strip(), loc=val("f_loc", "f_loc_other"),
             et=val("f_et", "f_et_other"), et_listed=ss.get("f_et") not in ("", OTHER), eq=val("f_eq", "f_eq_other"),
             area=ss.get("f_area", "").strip(), mo=ss["f_mo"], st=ss["f_st"], tags=list(ss.get("f_tags", [])))
    sig = json.dumps([BU["id"], R.fingerprint, J], sort_keys=True)

    def identify():
        need = [n for n, k in (("Job title", "jt"), ("Description", "desc"), ("Department / Section", "dept"), ("Assessed by", "by"),
                               ("Reviewed / Approved by", "rev"), ("Location of work", "loc"), ("Equipment type", "et"),
                               ("Specific equipment", "eq"), ("Specific work area", "area")) if not J[k]]
        if not J["tags"] and not J["et_listed"]:
            need.append("at least one activity (or a listed equipment type)")
        if need:
            ss["val_msg"] = need
            ss.pop("result", None)
            return
        ss.pop("val_msg", None)
        hz = collect_hazards(R, J["tags"], J["et"] if J["et_listed"] else None, J["mo"], J["st"])
        t = now()
        serial = make_serial(t, J["eq"], J["et"])
        ss["result"] = {"sig": sig, "hazards": hz, "serial": serial, "generated": t.strftime("%d %b %Y %H:%M WAT"), "iso": t.isoformat()}
        c = counts(hz)
        m = sorted(ss["methods"]) or ["From scratch"]
        log_event({"event": "generated", "time": t.isoformat(), "user": user.get("username"), "bu": BU["name"], "serial": serial,
                   "jobType": J["jt"], "description": J["desc"], "department": J["dept"], "location": J["loc"], "workArea": J["area"],
                   "equipmentType": J["et"], "equipmentRef": J["eq"], "motion": J["mo"], "status": J["st"],
                   "method": m[0] if len(m) == 1 else "Combination (" + " + ".join(m) + ")", "activities": "; ".join(J["tags"]),
                   "activityCount": len(J["tags"]), "hazardCount": len(hz), "extreme": c["E"], "high": c["H"], "moderate": c["M"],
                   "low": c["L"], "negligible": c["N"], "assessedBy": J["by"], "approvedBy": J["rev"], "registerFingerprint": R.fingerprint})

    if ss.get("val_msg"):
        st.markdown('<div class="valbanner"><b>Complete these before identifying hazards:</b><br>' +
                    esc(", ".join(ss["val_msg"])) + ".</div>", unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2])
    c1.button("Back to tasks", width="stretch", on_click=reset_job)
    c2.button("Identify hazards", type="primary", width="stretch", on_click=identify)

    # ---------------- 4. Review
    res = ss.get("result")
    if res and res["sig"] != sig:
        st.warning("The job details have changed since hazards were identified. Select **Identify hazards** again — "
                   "the review and PDF are hidden so they always match the inputs.")
    elif res:
        hz = res["hazards"]
        key = lambda h: f"inc_{res['serial']}_{h['uid']}"
        excluded = {h["uid"] for h in hz if not ss.get(key(h), True)}
        inc = [h for h in hz if h["uid"] not in excluded]
        c = counts(inc)
        st.markdown(f'<div class="report-banner"><div class="company">{esc(COMPANY)}</div>'
                    f'<div class="form-title">{esc(settings.get("FormTitle") or "RISK ASSESSMENT FORM")}</div></div>', unsafe_allow_html=True)
        header = [("Assessment No.", res["serial"]), ("Business unit", BU["name"]), ("Department / Section", J["dept"]),
                  ("Location of work", J["loc"]), ("Specific work area", J["area"]), ("Specific equipment", J["eq"]),
                  ("Equipment type", J["et"] + ("" if J["et_listed"] else " (unlisted - activity hazards only)")),
                  ("Motion / Status", f"{J['mo']} / {J['st']}"), ("Title of work", f"{J['jt']} — {J['eq']}"),
                  ("Description", J["desc"]), ("Activities", ", ".join(J["tags"]) or "none selected")]
        with st.container(border=True):
            st.markdown("".join(f'<div class="kv"><div class="k">{esc(k)}</div><div class="v">{esc(v)}</div></div>' for k, v in header),
                        unsafe_allow_html=True)
            if "draft" in settings.get("RegisterStatus", "").lower():
                st.warning(f"Register status: {settings['RegisterStatus']}. Hazards must be validated by the {BU['name']} HSE lead.")
            st.markdown(f'<div class="verify"><b>Verify before export.</b> Every hazard below is copied from the {esc(BU["name"])} register. '
                        f'Untick any that do not apply — they stay on the record, marked as reviewed and excluded.<br>'
                        f'<b>{len(inc)}</b> included · <b>{len(excluded)}</b> excluded</div>', unsafe_allow_html=True)
            strip = f'<span class="chip total">{len(inc)} HAZARDS</span>' + "".join(
                f'<span class="chip {k}">{c[k]} {LEVEL_NAME[k]}</span>' for k in "EHMLN" if c[k])
            if excluded:
                strip += f'<span class="chip X">{len(excluded)} EXCLUDED</span>'
            st.markdown(f'<div class="strip">{strip}</div>', unsafe_allow_html=True)
            if not hz:
                st.info("No hazards in the register match this selection. Add activities or choose a listed equipment type.")
            for n, cat in enumerate(CATS, 1):
                rows = [h for h in hz if h["cat"] == cat]
                st.markdown(f'<div class="sec">{n}. {esc(cat)}</div>', unsafe_allow_html=True)
                if not rows:
                    st.caption("No hazards in this category for the current selection.")
                for h in rows:
                    st.checkbox(f"Applies to this job · {h['id']}", value=True, key=key(h))
                    x = h["uid"] in excluded
                    st.markdown(
                        f'<div class="hcard{" x" if x else ""}"><div class="top"><div class="t">{esc(h["hz"])}</div>'
                        f'<span class="badge {esc(h["lv"])}">{esc(h["lv"])}</span></div><div class="c">{esc(h["ct"])}</div>'
                        f'<div class="r">↓ Residual risk after controls <span class="badge {esc(h["rd"])}">{esc(h["rd"])}</span></div>'
                        f'<div class="s">{esc(h["id"])} · {esc(h["src"])} · Responsible: {esc(h["rp"] or "—")}</div>'
                        + ('<div class="xtag">REVIEWED AND EXCLUDED BY ASSESSOR AS NOT APPLICABLE</div>' if x else "") + "</div>",
                        unsafe_allow_html=True)
            ppe = compile_ppe(inc)
            st.markdown(f'<div class="sec">PPE required (compiled from included hazards)</div>'
                        f'<div class="ppe">{esc("; ".join(ppe)) if ppe else "No PPE listed for the included hazards."}</div>', unsafe_allow_html=True)
            st.markdown('<div class="erp"><strong>Emergency Response Plan</strong>' + "<br>".join(esc(x) for x in ERP) + "</div>",
                        unsafe_allow_html=True)

        pdf = build_pdf({"bu": BU["name"], "company": COMPANY, "form_title": settings.get("FormTitle") or "RISK ASSESSMENT FORM",
                         "serial": res["serial"], "header": header, "hazards": hz, "excluded": excluded, "erp": ERP,
                         "assessed_by": J["by"], "reviewed_by": J["rev"], "generated": res["generated"], "fingerprint": R.fingerprint,
                         "register_status": settings.get("RegisterStatus", "")})
        st.download_button("Download PDF", data=pdf, file_name=f"Risk_Assessment_{res['serial']}.pdf", mime="application/pdf",
                           type="primary", width="stretch",
                           on_click=lambda: log_event({"event": "exported", "time": now().isoformat(), "user": user.get("username"),
                                                       "bu": BU["name"], "serial": res["serial"], "hazardCount": len(hz),
                                                       "hazardsIncluded": len(inc), "hazardsExcluded": len(excluded),
                                                       "registerFingerprint": R.fingerprint}))


with tab_build:
    render_build()

# ============================================================================ REGISTER
with tab_reg:
    with st.container(border=True):
        st.markdown("### Risk register")
        st.markdown(f'<p class="hint">{esc(BU["name"])} · {esc(Path(R.path).name)} · fingerprint <b>{R.fingerprint}</b></p>', unsafe_allow_html=True)
        views = {
            "Activity hazards": lambda: pd.DataFrame([{"ID": h["id"], "Activity": h["key"], "Category": h["cat"], "Hazard": h["hz"], "Level": h["lv"],
                                                       "Controls": h["ct"], "Residual": h["rd"], "Responsible": h["rp"], "PPE": "; ".join(h["ppe"]),
                                                       "Motion": h["mo"], "Status": h["st"]} for h in R.activity_hazards]),
            "Equipment hazards": lambda: pd.DataFrame([{"ID": h["id"], "Equipment type": h["key"], "Category": h["cat"], "Hazard": h["hz"],
                                                        "Level": h["lv"], "Controls": h["ct"], "Residual": h["rd"], "Responsible": h["rp"],
                                                        "PPE": "; ".join(h["ppe"]), "Motion": h["mo"], "Status": h["st"]} for h in R.equipment_hazards]),
            "Activities": lambda: pd.DataFrame([{"ID": t["id"], "Activity": t["t"], "Category": t["c"]} for t in R.job_tags]),
            "Equipment types": lambda: pd.DataFrame({"Equipment type": R.equipment_types}),
            "Locations": lambda: pd.DataFrame([{"Location": l["n"], "Type": l["type"],
                                                "Equipment available": sum(R.available(e, l["n"]) for e in R.equipment)} for l in R.locations]),
            "Equipment": lambda: pd.DataFrame([{"ID": e["id"], "Equipment": e["n"], "Type": e["t"],
                                                "Found in": e["scope"] if e["scope"] != "Listed areas only" else "; ".join(e["locs"])} for e in R.equipment]),
            "Presets": lambda: pd.DataFrame([{"Preset": p["n"], "Category": p["cat"], "Description": p["d"], "Equipment": p["ref"],
                                              "Area": p["loc"], "Activities": "; ".join(p["tags"])} for p in R.presets]),
            "Tools": lambda: pd.DataFrame([{"Tool phrase": t["p"], "Category": t["c"], "Activities": "; ".join(t["tags"])} for t in R.tools]),
            "Inference rules": lambda: pd.DataFrame([{"ID": r["id"], "Label": r["label"], "Trigger": r["trig"].pattern,
                                                      "Also requires": r["also"].pattern, "Activities": "; ".join(r["tags"])} for r in R.rules]),
        }
        v = st.selectbox("View", list(views), key="reg_view", label_visibility="collapsed")
        f = st.text_input("Search the register", key="reg_q", placeholder="Search…", label_visibility="collapsed").lower().strip()
        df = views[v]()
        if f and not df.empty:
            df = df[df.apply(lambda r: f in " ".join(map(str, r.values)).lower(), axis=1)]
        st.caption(f"{len(df)} rows")
        st.dataframe(df, width="stretch", hide_index=True, height=420)
        st.download_button("Download this register (.xlsx)", data=Path(R.path).read_bytes(), file_name=Path(R.path).name,
                           mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", width="stretch")
    with st.expander("Assessment log (this server)"):
        if LOG.exists():
            lg = pd.read_csv(LOG)
            st.dataframe(lg.tail(50).iloc[::-1], width="stretch", hide_index=True)
            st.download_button("Download log (CSV)", data=LOG.read_bytes(), file_name="assessment_log.csv", mime="text/csv")
        else:
            st.caption("No assessments generated on this server yet.")
        st.caption("On Streamlit Community Cloud this file resets when the app restarts — download it regularly or move it to SharePoint.")
