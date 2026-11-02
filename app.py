"""Risk Assessment Generator - Streamlit, multi-business-unit (v5.2).

sign in -> select business unit -> Build (job -> hazards -> review -> PDF) | Register (view) | Admin (password: upload, log, password)
Each business unit uses only its own register. Refinery and fertiliser have built-in default registers.
"""
from __future__ import annotations

import html
import json
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd
import streamlit as st

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))
if not (_HERE / "ra" / "engine.py").exists():
    st.error("The app files are incomplete: the **ra** folder (engine.py, store.py, auth.py, theme.py, pdf_report.py, __init__.py and the "
             "defaults sub-folder) must sit next to app.py in the GitHub repo. Upload the whole package with its folders.")
    st.stop()

from ra import adminlog, auth, store, theme  # noqa: E402
from ra.engine import (LEVEL_NAME, OTHER_LOC_NAME, RegisterError, blank_template_bytes, collect_hazards,  # noqa: E402
                       compile_ppe, counts, load_register_bytes, make_serial, suggest_from_text)
from ra.pdf_report import build_pdf, build_register_request_pdf  # noqa: E402

TZ = ZoneInfo("Africa/Lagos")
OTHER = "__other__"
XLSX = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
st.set_page_config(page_title="Risk Assessment Generator", page_icon="🦺", layout="centered")
theme.apply()
ss = st.session_state


# ============================================================================ helpers
def load_bus() -> list[dict]:
    return json.loads((_HERE / "bu_config.json").read_text(encoding="utf-8"))["business_units"]


def esc(x) -> str:
    return html.escape(str(x or ""))


def now() -> datetime:
    return datetime.now(TZ)


FIELDS = ["f_jt", "f_desc", "f_dept", "f_by", "f_rev", "f_loc", "f_loc_other", "f_et", "f_et_other", "f_eq", "f_eq_other", "f_area", "f_mo", "f_st", "f_tags"]


def reset_job():
    for k in list(ss.keys()):
        if k in FIELDS or k.startswith("inc_") or k in ("result", "started", "methods", "suggest_msg", "val_msg", "preset_q"):
            del ss[k]


def set_bu(bu_id):
    reset_job()
    ss.pop("bu_pick", None)
    if bu_id:
        ss["bu_id"] = bu_id
    else:
        ss.pop("bu_id", None)


# ============================================================================ sign-in + BU
user = auth.require_sign_in(lambda: theme.appbar())
BUS = load_bus()
BU_BY_ID = {b["id"]: b for b in BUS}

with st.sidebar:
    st.markdown(f"**Signed in:** {esc(user.get('name') or user.get('username'))}")
    if auth.test_account_active() and user.get("username") == auth.TEST_USER:
        st.warning("Test account in use - add real users in Secrets before live use.")

    def _sign_out():
        auth.sign_out()
        set_bu(None)
    st.button("Sign out", width="stretch", on_click=_sign_out)
    if ss.get("bu_id") in BU_BY_ID:
        st.divider()
        st.markdown(f"**Business unit:** {esc(BU_BY_ID[ss['bu_id']]['name'])}")
        st.button("Change business unit", width="stretch", on_click=set_bu, args=(None,))

if ss.get("bu_id") not in BU_BY_ID:
    theme.appbar()
    with st.container(border=True):
        st.markdown("### Select business unit")
        st.markdown('<p class="hint">Hazards are taken only from the selected business unit\'s own risk register.</p>', unsafe_allow_html=True)
        status = {b["id"]: store.resolve(b) for b in BUS}
        choice = st.selectbox("Business unit", [b["id"] for b in BUS], index=None, key="bu_pick", placeholder="— select business unit —",
                              format_func=lambda i: BU_BY_ID[i]["name"] + ("" if status[i][0] else "  (no register)"))
        for b in BUS:
            reg, src, why = status[b["id"]]
            state = (f'<span class="ok">{esc(src)}</span> · {reg.hazard_count} hazards · fingerprint {reg.fingerprint}' if reg
                     else f'<span class="bad">No usable register</span> · {esc(why)}')
            st.markdown(f'<div class="bu-card"><div class="n">{esc(b["name"])}</div><div class="d">{state}</div></div>', unsafe_allow_html=True)
        st.button("Continue", type="primary", width="stretch", disabled=choice is None, on_click=set_bu, args=(choice,))
    st.stop()

BU = BU_BY_ID[ss["bu_id"]]
R, REG_SRC, REG_NOTE = store.resolve(BU)
settings = R.settings if R else {}
COMPANY = settings.get("CompanyName") or BU.get("company") or BU["name"].upper()
ERP = [settings[k] for k in ("ERP1", "ERP2", "ERP3", "ERP4") if settings.get(k)] or BU.get("erp") or \
      ["Emergency contact numbers for this business unit have not been set - add ERP lines to the register's Settings sheet."]
theme.appbar(BU["name"])
if REG_NOTE and R:
    st.warning(REG_NOTE)

if R:
    st.sidebar.caption(f"Register: **{REG_SRC}** · fingerprint **{R.fingerprint}** · {len(R.activity_hazards)} activity + "
                       f"{len(R.equipment_hazards)} equipment hazards")
    if settings.get("RegisterStatus"):
        st.sidebar.info(f"Register status: {settings['RegisterStatus']}")
    if R.warnings:
        with st.sidebar.expander(f"Register check: {len(R.warnings)} issue(s)"):
            for w in R.warnings[:60]:
                st.caption(w)

if ss.get("admin_msg"):
    st.success(ss.pop("admin_msg"))
tab_names = (["Build", "Register"] if R else ["Register update required"]) + ["Admin"]
tabs = dict(zip(tab_names, st.tabs(tab_names)))


# ============================================================================ NO REGISTER
def render_no_register():
    st.markdown(f'<div class="noreg"><h4>Risk register update required</h4>Risk assessments cannot be generated for <b>{esc(BU["name"])}</b>. '
                f'{esc(REG_NOTE)}<br>Every hazard in an assessment must come from the business unit\'s own approved register, so the register '
                f'owner (<b>{esc(BU.get("register_owner", "BU HSE"))}</b>) needs to provide it'
                + " — or upload it on the <b>Admin</b> tab." + "</div>", unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown("### Register update request")
        c1, c2 = st.columns(2)
        req_by = c1.text_input("Requested by", value=user.get("name", ""))
        req_dept = c2.text_input("Department / section")
        req_note = st.text_area("Work you need to assess (optional)")
        when = now().strftime("%d %b %Y %H:%M")
        req = {"bu": BU["name"], "when": when, "rows": [("Business unit", BU["name"]), ("Register owner", BU.get("register_owner", "")),
               ("Register status", REG_NOTE or ""), ("Requested by", req_by or "-"), ("Department / section", req_dept or "-"),
               ("Work to be assessed", req_note or "-"), ("Date of request", when)]}
        st.download_button("Download update request (PDF)", data=build_register_request_pdf(req), type="primary", width="stretch",
                           file_name=f"Register_Update_Request_{BU['id']}_{now():%Y%m%d}.pdf", mime="application/pdf")
        st.download_button("Download blank register template (.xlsx)", data=blank_template_bytes(BU["name"]),
                           file_name=f"{BU['id'].upper()}_Risk_Register_TEMPLATE.xlsx", mime=XLSX, width="stretch")


# ============================================================================ BUILD
def render_build():
    TAGCAT = {t["t"]: t["c"] for t in R.job_tags}
    order = {"Process": 0, "Utility": 1, "Site": 2, "Building": 3, "Other": 4}
    LOCS = [l["n"] for l in sorted(R.locations, key=lambda l: order.get(l["type"], 5)) if l["n"] != OTHER_LOC_NAME]
    ss.setdefault("methods", set())

    def apply_preset(p):
        reset_job()
        ss.update(f_jt=p["n"], f_desc=p["d"], f_tags=[t for t in p["tags"] if t in TAGCAT], f_loc=p["loc"] if p["loc"] in LOCS else "",
                  f_et=p["et"] if p["et"] in R.equipment_types else "", f_eq=p["ref"] if R.equip(p["ref"]) else "",
                  f_mo=p["mo"] if p["mo"] in R.motions else R.motions[0], f_st=p["st"] if p["st"] in R.statuses else R.statuses[0],
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
            ss["f_et"] = eq["t"]

    def do_suggest():
        s = suggest_from_text(R, f"{ss.get('f_jt', '')}. {ss.get('f_desc', '')}")
        before = set(ss.get("f_tags", []))
        ss["f_tags"] = list(before | set(s["tags"]))
        added = [t for t in s["tags"] if t not in before]
        msg = ["Added: " + "; ".join(f"**{t}** ({s['reasons'][t]})" for t in added)] if added else []
        if s["equipment"] and not ss.get("f_eq"):
            ss["f_eq"], ss["f_et"] = s["equipment"], s["equipment_type"]
            msg.append(f"Equipment set to **{s['equipment']}**")
        if s["motion"]:
            ss["f_mo"], ss["f_st"] = s["motion"], s["status"]
            msg.append(f"Motion/status set to **{s['motion']} / {s['status']}**")
        ss["suggest_msg"] = "  \n".join(msg) or "Nothing new recognised - add activities from the list below."
        ss["methods"].add("Description assist")

    if not ss.get("started"):
        with st.container(border=True):
            st.markdown("### Start from a common task")
            st.markdown('<p class="hint">Tap a job you\'re about to do. It fills in the activities and equipment for you — you can adjust everything afterwards.</p>',
                        unsafe_allow_html=True)
            q = st.text_input("Search tasks", key="preset_q", placeholder="Search tasks…", label_visibility="collapsed").lower().strip()
            plist = [p for p in R.presets if not q or q in f"{p['n']} {p['d']} {p['cat']} {' '.join(p['tags'])}".lower()]
            if not R.presets:
                st.caption("This register has no task presets.")
            elif not plist:
                st.caption("No matching tasks — try “start from scratch” below.")
            for cat in dict.fromkeys(p["cat"] for p in plist):
                with st.expander(f"{cat}  ·  {sum(p['cat'] == cat for p in plist)}", expanded=bool(q)):
                    for i, p in enumerate(x for x in plist if x["cat"] == cat):
                        st.markdown(f"**{esc(p['n'])}**  \n<span class='hint'>{esc(p['d'])} · {len(p['tags'])} activities · {esc(p['loc'] or 'choose area')}</span>",
                                    unsafe_allow_html=True)
                        st.button("Use this task", key=f"pre_{cat}_{i}_{p['id']}", on_click=apply_preset, args=(p,))
            st.button("Start from scratch", width="stretch", on_click=start_scratch)
        return

    with st.container(border=True):
        st.markdown("### 1 · Job details")
        st.text_input("Job title *", key="f_jt")
        st.text_area("Description *", key="f_desc", placeholder="Task, tools and method")
        st.button("Suggest activities from description", on_click=do_suggest)
        if ss.get("suggest_msg"):
            st.info(ss["suggest_msg"])
        st.text_input("Department / Section *", key="f_dept")
        c1, c2 = st.columns(2)
        c1.text_input("Assessed by *", key="f_by")
        c2.text_input("Reviewed / Approved by *", key="f_rev")

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
            st.caption("An unlisted equipment type has no equipment hazards in the register, so only activity hazards will be generated.")
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
        st.text_input("Specific work area *", key="f_area")
        if ss.get("f_mo") not in R.motions:
            ss["f_mo"] = R.motions[0]
        if ss.get("f_st") not in R.statuses:
            ss["f_st"] = R.statuses[0]
        c1, c2 = st.columns(2)
        c1.selectbox("Motion", R.motions, key="f_mo")
        c2.selectbox("Status", R.statuses, key="f_st")

    with st.container(border=True):
        ss["f_tags"] = [t for t in ss.get("f_tags", []) if t in TAGCAT]
        st.markdown(f"### 3 · Activities · {len(ss['f_tags'])}")
        st.multiselect("Activities", R.tag_names, key="f_tags", format_func=lambda t: f"{t}  ·  {TAGCAT.get(t, '')}",
                       placeholder="Search activities…", label_visibility="collapsed")

    def val(k, other):
        v = ss.get(k, "")
        return (ss.get(other, "") or "").strip() if v == OTHER else v

    J = dict(jt=ss.get("f_jt", "").strip(), desc=ss.get("f_desc", "").strip(), dept=ss.get("f_dept", "").strip(), by=ss.get("f_by", "").strip(),
             rev=ss.get("f_rev", "").strip(), loc=val("f_loc", "f_loc_other"), et=val("f_et", "f_et_other"), et_listed=ss.get("f_et") not in ("", OTHER),
             eq=val("f_eq", "f_eq_other"), area=ss.get("f_area", "").strip(), mo=ss["f_mo"], st=ss["f_st"], tags=list(ss.get("f_tags", [])))
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
        ss["result"] = {"sig": sig, "hazards": hz, "serial": serial, "generated": t.strftime("%d %b %Y %H:%M WAT")}
        c = counts(hz)
        m = sorted(ss["methods"]) or ["From scratch"]
        adminlog.append_log({"serial": serial, "generatedAt": t.isoformat(timespec="seconds"), "businessUnit": BU["name"],
                             "registerFingerprint": R.fingerprint, "jobType": J["jt"], "equipmentType": J["et"], "equipmentRef": J["eq"],
                             "equipmentMotion": J["mo"], "equipmentStatus": J["st"], "location": J["loc"], "workArea": J["area"],
                             "department": J["dept"], "generationMethod": m[0] if len(m) == 1 else "Combination (" + " + ".join(m) + ")",
                             "activityCount": len(J["tags"]), "hazardCount": len(hz), "hazardsIncluded": len(hz), "hazardsExcluded": 0,
                             "exportedAt": "", "extreme": c["E"], "high": c["H"], "moderate": c["M"], "low": c["L"], "negligible": c["N"],
                             "assessedBy": J["by"], "approvedBy": J["rev"], "activities": J["tags"], "user": user.get("username", "")})

    if ss.get("val_msg"):
        st.markdown('<div class="valbanner"><b>Complete these before identifying hazards:</b><br>' + esc(", ".join(ss["val_msg"])) + ".</div>",
                    unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2])
    c1.button("Back to tasks", width="stretch", on_click=reset_job)
    c2.button("Identify hazards", type="primary", width="stretch", on_click=identify)

    res = ss.get("result")
    if res and res["sig"] != sig:
        st.warning("The job details (or the register) have changed since hazards were identified. Select **Identify hazards** again — "
                   "the review and PDF are hidden so they always match the inputs.")
        return
    if not res:
        return
    hz = res["hazards"]
    key = lambda h: f"inc_{res['serial']}_{h['uid']}"
    excluded = {h["uid"] for h in hz if not ss.get(key(h), True)}
    inc = [h for h in hz if h["uid"] not in excluded]
    c = counts(inc)
    st.markdown(f'<div class="report-banner"><div class="company">{esc(COMPANY)}</div>'
                f'<div class="form-title">{esc(settings.get("FormTitle") or "RISK ASSESSMENT FORM")}</div></div>', unsafe_allow_html=True)
    header = [("Assessment No.", res["serial"]), ("Business unit", BU["name"]), ("Department / Section", J["dept"]), ("Location of work", J["loc"]),
              ("Specific work area", J["area"]), ("Specific equipment", J["eq"]),
              ("Equipment type", J["et"] + ("" if J["et_listed"] else " (unlisted - activity hazards only)")), ("Motion / Status", f"{J['mo']} / {J['st']}"),
              ("Title of work", f"{J['jt']} — {J['eq']}"), ("Description", J["desc"]), ("Activities", ", ".join(J["tags"]) or "none selected")]
    with st.container(border=True):
        st.markdown("".join(f'<div class="kv"><div class="k">{esc(k)}</div><div class="v">{esc(v)}</div></div>' for k, v in header), unsafe_allow_html=True)
        if "draft" in settings.get("RegisterStatus", "").lower():
            st.warning(f"Register status: {settings['RegisterStatus']}. Hazards must be validated by the {BU['name']} HSE lead.")
        st.markdown(f'<div class="verify"><b>Verify before export.</b> Every hazard below is copied from the {esc(BU["name"])} register. Untick any that do '
                    f'not apply — they stay on the record, marked as reviewed and excluded.<br><b>{len(inc)}</b> included · <b>{len(excluded)}</b> excluded</div>',
                    unsafe_allow_html=True)
        strip = f'<span class="chip total">{len(inc)} HAZARDS</span>' + "".join(f'<span class="chip {k}">{c[k]} {LEVEL_NAME[k]}</span>' for k in "EHMLN" if c[k])
        if excluded:
            strip += f'<span class="chip X">{len(excluded)} EXCLUDED</span>'
        st.markdown(f'<div class="strip">{strip}</div>', unsafe_allow_html=True)
        if not hz:
            st.info("No hazards in the register match this selection. Add activities or choose a listed equipment type.")
        for n, cat in enumerate(R.categories, 1):
            rows = [h for h in hz if h["cat"] == cat]
            st.markdown(f'<div class="sec">{n}. {esc(cat)}</div>', unsafe_allow_html=True)
            if not rows:
                st.caption("No hazards in this category for the current selection.")
            for h in rows:
                st.checkbox(f"Applies to this job · {h['id']}", value=True, key=key(h))
                x = h["uid"] in excluded
                st.markdown(f'<div class="hcard{" x" if x else ""}"><div class="top"><div class="t">{esc(h["hz"])}</div><span class="badge {esc(h["lv"])}">'
                            f'{esc(h["lv"])}</span></div><div class="c">{esc(h["ct"])}</div><div class="r">↓ Residual risk after controls '
                            f'<span class="badge {esc(h["rd"])}">{esc(h["rd"])}</span></div><div class="s">{esc(h["id"])} · {esc(h["src"])} · Responsible: '
                            f'{esc(h["rp"] or "—")}</div>' + ('<div class="xtag">REVIEWED AND EXCLUDED BY ASSESSOR AS NOT APPLICABLE</div>' if x else "") + "</div>",
                            unsafe_allow_html=True)
        ppe = compile_ppe(inc)
        st.markdown(f'<div class="sec">PPE required (compiled from included hazards)</div><div class="ppe">'
                    f'{esc("; ".join(ppe)) if ppe else "No PPE listed for the included hazards."}</div>', unsafe_allow_html=True)
        st.markdown('<div class="erp"><strong>Emergency Response Plan</strong>' + "<br>".join(esc(x) for x in ERP) + "</div>", unsafe_allow_html=True)
    pdf = build_pdf({"bu": BU["name"], "company": COMPANY, "form_title": settings.get("FormTitle") or "RISK ASSESSMENT FORM", "serial": res["serial"],
                     "header": header, "hazards": hz, "excluded": excluded, "erp": ERP, "assessed_by": J["by"], "reviewed_by": J["rev"],
                     "generated": res["generated"], "fingerprint": R.fingerprint, "register_status": settings.get("RegisterStatus", ""),
                     "categories": R.categories, "register_source": REG_SRC})
    st.download_button("Download PDF", data=pdf, file_name=f"Risk_Assessment_{res['serial']}.pdf", mime="application/pdf", type="primary", width="stretch",
                       on_click=lambda: adminlog.mark_exported(res["serial"], now().isoformat(timespec="seconds"), len(inc), len(excluded)))


# ============================================================================ REGISTER VIEW
def render_register_view():
    with st.container(border=True):
        st.markdown("### Risk register")
        st.markdown(f'<p class="hint">{esc(BU["name"])} · <span class="src-pill">{esc(REG_SRC)}</span> · fingerprint <b>{R.fingerprint}</b></p>',
                    unsafe_allow_html=True)
        hzdf = lambda lst, col: pd.DataFrame([{"ID": h["id"], col: h["key"], "Category": h["cat"], "Hazard": h["hz"], "Level": h["lv"], "Controls": h["ct"],
                                               "Residual": h["rd"], "Responsible": h["rp"], "PPE": "; ".join(h["ppe"]), "Motion": h["mo"], "Status": h["st"]}
                                              for h in lst])
        views = {
            "Activity hazards": lambda: hzdf(R.activity_hazards, "Activity"),
            "Equipment hazards": lambda: hzdf(R.equipment_hazards, "Equipment type"),
            "Activities": lambda: pd.DataFrame([{"ID": t["id"], "Activity": t["t"], "Category": t["c"]} for t in R.job_tags]),
            "Locations": lambda: pd.DataFrame([{"Location": l["n"], "Type": l["type"], "Equipment available": sum(R.available(e, l["n"]) for e in R.equipment)}
                                               for l in R.locations]),
            "Equipment": lambda: pd.DataFrame([{"ID": e["id"], "Equipment": e["n"], "Type": e["t"],
                                                "Found in": e["scope"] if e["scope"] != "Listed areas only" else "; ".join(e["locs"])} for e in R.equipment]),
            "Presets": lambda: pd.DataFrame([{"Preset": p["n"], "Category": p["cat"], "Equipment": p["ref"], "Area": p["loc"], "Activities": "; ".join(p["tags"])}
                                             for p in R.presets]),
            "Tools": lambda: pd.DataFrame([{"Tool phrase": t["p"], "Category": t["c"], "Activities": "; ".join(t["tags"])} for t in R.tools]),
            "Synonyms": lambda: pd.DataFrame([{"Phrase": x["p"], "Activity": x["t"]} for x in R.synonyms]),
            "Inference rules": lambda: pd.DataFrame([{"ID": r["id"], "Label": r["label"], "Trigger": r["trig"].pattern, "Also requires": r["also"].pattern,
                                                      "Activities": "; ".join(r["tags"])} for r in R.rules]),
        }
        v = st.selectbox("View", list(views), key="reg_view", label_visibility="collapsed")
        f = st.text_input("Search the register", key="reg_q", placeholder="Search…", label_visibility="collapsed").lower().strip()
        df = views[v]()
        if f and not df.empty:
            df = df[df.apply(lambda r: f in " ".join(map(str, r.values)).lower(), axis=1)]
        st.caption(f"{len(df)} rows")
        st.dataframe(df, width="stretch", hide_index=True, height=420)
        st.download_button("Download this register (.xlsx)", data=Path(R.path).read_bytes(), file_name=Path(BU.get("register") or R.path).name,
                           mime=XLSX, width="stretch")


# ============================================================================ ADMIN (ported from the original HTML app)
def render_admin():
    if not ss.get("admin_unlocked"):
        with st.container(border=True):
            st.markdown('<div style="text-align:center;font-size:32px;margin:8px 0 4px;">🔒</div>', unsafe_allow_html=True)
            st.markdown('<h3 style="text-align:center;">Admin Access</h3>', unsafe_allow_html=True)
            st.markdown('<p class="hint" style="text-align:center;">Enter the admin password to manage app data.</p>', unsafe_allow_html=True)
            with st.form("gate"):
                pw = st.text_input("Password", type="password", label_visibility="collapsed", placeholder="Password")
                go = st.form_submit_button("Unlock", type="primary", width="stretch")
            if go:
                if not pw:
                    st.error("Enter the admin password.")
                elif adminlog.verify_admin(pw):
                    ss["admin_unlocked"] = True
                    st.rerun()
                else:
                    st.error("Incorrect password.")
            if adminlog.cred_source() == "built-in default":
                st.caption(f"Default admin password: `{adminlog.DEFAULT_ADMIN_PASSWORD}` — change it under **Admin password** after unlocking.")
        return

    # ---------------- Manage Data
    with st.container(border=True):
        st.markdown("### Manage Data")
        st.markdown(f'<p class="hint">Business unit: <b>{esc(BU["name"])}</b>. Download the master workbook to edit offline, or upload an updated .xlsx with '
                    'sheets named <b>JobTags</b>, <b>EquipmentTypes</b>, <b>Equipment</b>, <b>ActivityHazards</b>, <b>EquipmentHazards</b>, '
                    '<b>TaskPresets</b>, <b>Locations</b> and <b>ToolRecognition</b>. Other business units are not affected.</p>', unsafe_allow_html=True)
        up = st.file_uploader("Choose an updated workbook", type=["xlsx"], key=f"up_{BU['id']}_{ss.get('up_n', 0)}")
        if up is not None:
            data = up.getvalue()
            try:
                NEW = load_register_bytes(data, store.TMP_DIR / BU["id"], "candidate.xlsx")
                unit = NEW.settings.get("BusinessUnit", "").strip()
                if unit and unit.lower() != BU["name"].strip().lower():
                    raise RegisterError(f"the workbook's Settings sheet says it belongs to '{unit}', not '{BU['name']}'. "
                                        "Select the right business unit, or correct BusinessUnit on the Settings sheet.")
                store.activate(BU, data, user.get("username", ""), up.name, NEW.fingerprint)
                msg = (f"Loaded {up.name}: {len(NEW.activity_hazards)} activity + {len(NEW.equipment_hazards)} equipment hazards, "
                       f"{len(NEW.job_tags)} activities, {len(NEW.equipment)} equipment, {len(NEW.presets)} presets.")
                if NEW.warnings:
                    msg += f" {len(NEW.warnings)} consistency issue(s) — see 'Register check' in the sidebar."
                if store.github_cfg():
                    try:
                        store.github_commit(BU, data, user.get("username", ""), up.name)
                        msg += " Saved permanently to the GitHub repo."
                    except Exception as exc:
                        msg += f" GitHub save failed ({exc}) — active on this server only."
                ss["upload_status"] = ("success", msg)
                reset_job()
            except RegisterError as exc:
                ss["upload_status"] = ("error", f"Could not load {up.name}: {exc}")
            ss["up_n"] = ss.get("up_n", 0) + 1
            st.rerun()
        if ss.get("upload_status"):
            kind, msg = ss["upload_status"]
            (st.success if kind == "success" else st.error)(msg)
        if R:
            meta = store.read_meta(BU) if REG_SRC == "Uploaded" else {}
            st.markdown(
                f'<div class="ppe" style="margin-top:8px;"><b>Current data</b> · {esc(REG_SRC)}'
                + (f' ({esc(meta.get("note", ""))}, {esc(meta.get("uploaded_by", ""))}, {esc(meta.get("uploaded_at", "").replace("T", " "))})' if meta else "")
                + f'<br><b>{len(R.activity_hazards)}</b> activity hazards · <b>{len(R.equipment_hazards)}</b> equipment hazards<br>'
                f'<b>{len(R.job_tags)}</b> activities · <b>{len(R.equipment_types)}</b> equipment types · <b>{len(R.equipment)}</b> equipment<br>'
                f'<b>{len(R.locations)}</b> locations · <b>{len(R.presets)}</b> presets · <b>{len(R.tools)}</b> tools<br>'
                f'Fingerprint <b>{R.fingerprint}</b></div>', unsafe_allow_html=True)
            st.download_button("Download Master Workbook", data=Path(R.path).read_bytes(), mime=XLSX, width="stretch",
                               file_name=Path(BU.get("register") or R.path).name)
        else:
            st.markdown(f'<div class="valbanner">No register loaded for this business unit. {esc(REG_NOTE)}</div>', unsafe_allow_html=True)
            st.download_button("Download blank register template", data=blank_template_bytes(BU["name"]), mime=XLSX, width="stretch",
                               file_name=f"{BU['id'].upper()}_Risk_Register_TEMPLATE.xlsx")
        if REG_SRC == "Uploaded" and store.default_path(BU) is not None:
            def _restore():
                store.revert_to_default(BU)
                reset_job()
                ss["upload_status"] = ("success", "Restored the built-in default register.")
            st.button("Restore built-in default register", width="stretch", on_click=_restore)
        if not store.github_cfg():
            st.caption("On Streamlit Community Cloud an uploaded workbook lasts until the app restarts. Add a [github] section to Secrets "
                       "(see README) to save uploads permanently.")

    # ---------------- Assessment log
    with st.container(border=True):
        st.markdown("### Assessment Log")
        log = adminlog.read_log()
        mine = [x for x in log if x.get("businessUnit") == BU["name"]]
        scope = st.radio("Show", [f"{BU['name']} only", "All business units"], horizontal=True, key="log_scope", label_visibility="collapsed")
        rows = mine if scope.endswith("only") else log
        if not rows:
            st.markdown('<div class="ppe">No assessments generated on this server yet.<br>The log fills automatically each time an assessment is generated.</div>',
                        unsafe_allow_html=True)
        else:
            ext = sum(int(x.get("extreme") or 0) for x in rows)
            haz = sum(int(x.get("hazardCount") or 0) for x in rows)
            st.markdown(f'<div class="ppe"><b>{len(rows)}</b> assessments generated since {esc(rows[-1].get("generatedAt", "")[:10])}<br>'
                        f'<b>{haz}</b> hazards assessed in total &nbsp; <b>{ext}</b> extreme-rated</div>', unsafe_allow_html=True)
            for x in rows[:60]:
                try:
                    when = datetime.fromisoformat(x["generatedAt"]).strftime("%d %b %Y, %H:%M")
                except Exception:
                    when = x.get("generatedAt", "")
                extra = (f" · {x['hazardsExcluded']} excluded by assessor" if x.get("hazardsExcluded") else "") + \
                        (f" · {x['extreme']} extreme" if x.get("extreme") else "")
                st.markdown(
                    f'<div class="hcard" style="margin:6px 0;"><div class="s">{esc(x.get("serial"))}</div><div class="c" style="margin-top:2px;">'
                    f'<b>{esc(x.get("jobType") or "(no job type)")}</b>' + (f' · {esc(x.get("businessUnit"))}' if not scope.endswith("only") else "") +
                    f'<br>{esc(x.get("equipmentRef") or x.get("equipmentType"))} · {esc(x.get("equipmentMotion"))} / {esc(x.get("equipmentStatus"))}<br>'
                    f'{when} · {x.get("activityCount", 0)} activities · {x.get("hazardCount", 0)} hazards'
                    + (f'<br>Method: {esc(x.get("generationMethod"))}' if x.get("generationMethod") else "") + esc(extra)
                    + (f'<br>Assessed by: {esc(x.get("assessedBy"))}' if x.get("assessedBy") else "")
                    + ("" if x.get("exportedAt") else "<br><i>PDF not downloaded</i>") + "</div></div>", unsafe_allow_html=True)
            if len(rows) > 60:
                st.caption(f"Showing 60 most recent of {len(rows)}. Export for the full record.")
        tag = "ALL" if not scope.endswith("only") else BU["id"].upper()
        c1, c2, c3 = st.columns(3)
        c1.download_button("Export CSV", data=adminlog.log_csv(rows), file_name=f"Assessment_Log_{tag}_{now():%Y-%m-%d}.csv", mime="text/csv",
                           width="stretch", disabled=not rows)
        c2.download_button("Export JSON", data=json.dumps(rows, indent=2, ensure_ascii=False), width="stretch", disabled=not rows,
                           file_name=f"Assessment_Log_{tag}_{now():%Y-%m-%d}.json", mime="application/json")
        if c3.button("Clear log", width="stretch", disabled=not rows):
            ss["confirm_clear"] = True
        if ss.get("confirm_clear"):
            st.warning(f"Permanently delete all {len(rows)} log entries shown ({scope.lower()}) on this server? Export first if you need the record.")
            d1, d2 = st.columns(2)
            if d1.button("Delete permanently", type="primary", width="stretch"):
                keep = [x for x in log if x.get("businessUnit") != BU["name"]] if scope.endswith("only") else []
                adminlog.write_log(keep)
                ss.pop("confirm_clear", None)
                ss["upload_status"] = ("success", "Assessment log cleared.")
                st.rerun()
            if d2.button("Cancel", width="stretch"):
                ss.pop("confirm_clear", None)
                st.rerun()
        st.caption("On Streamlit Community Cloud the log resets when the app restarts — export it regularly.")

    # ---------------- Admin password
    with st.container(border=True):
        st.markdown("### Admin password")
        st.markdown(f'<p class="hint">Current password source: {esc(adminlog.cred_source())}.</p>', unsafe_allow_html=True)
        with st.form("pwchange", clear_on_submit=True):
            p1 = st.text_input("New password", type="password")
            p2 = st.text_input("Confirm new password", type="password")
            ok = st.form_submit_button("Change password", width="stretch")
        if ok:
            if len(p1) < 8:
                st.error("Use at least 8 characters.")
            elif p1 != p2:
                st.error("The passwords do not match.")
            else:
                adminlog.change_admin(p1, user.get("username", ""))
                st.success("Admin password changed on this server. For a permanent password on Streamlit Cloud, run "
                           "make_password_hash.py and put the hash under [admin] password_hash in Secrets.")
        st.button("Lock admin", width="stretch", on_click=lambda: ss.pop("admin_unlocked", None))


# ============================================================================ render
if R:
    with tabs["Build"]:
        render_build()
    with tabs["Register"]:
        render_register_view()
else:
    with tabs["Register update required"]:
        render_no_register()
with tabs["Admin"]:
    render_admin()
