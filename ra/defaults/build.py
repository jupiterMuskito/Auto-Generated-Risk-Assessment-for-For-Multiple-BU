"""Builds a business unit's built-in default workbook (same schema as OKPELLA_Master_Workbook_v8 + Settings + Synonyms).

Each business unit has its own independent source module in this folder. Nothing is shared between them.
Run from the app root:  python -m ra.defaults.build registers
"""
from __future__ import annotations

import importlib
import sys
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.workbook.defined_name import DefinedName
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.worksheet.table import Table, TableStyleInfo

SOURCES = {"refinery": "ra.defaults.refinery", "fertiliser": "ra.defaults.fertiliser"}
CAT = {"J": "Job Related Hazard", "L": "Job Location Related Hazard", "E": "Equipment and Material Related Hazard"}
HDR_FILL = PatternFill("solid", start_color="123A73")
HDR_FONT = Font(name="Arial", bold=True, color="FFFFFF", size=10)
BODY = Font(name="Arial", size=10)
NOTE = Font(name="Arial", italic=True, size=10, color="5C7086")
TITLE = Font(name="Arial", bold=True, size=14, color="123A73")
SECTION = Font(name="Arial", bold=True, size=10, color="123A73")
WRAP = Alignment(wrap_text=True, vertical="top")
TOP = Alignment(vertical="top")


def _rows(text):
    out = []
    for ln in text.strip().splitlines():
        p = ln.split("|")
        if len(p) not in (8, 10):
            raise ValueError("Bad hazard row: " + ln)
        tag, c, hz, lv, ct, rd, rp, ppe = p[:8]
        mo, st = (p[8], p[9]) if len(p) == 10 else ("Any", "Any")
        out.append(dict(key=tag, cat=CAT[c], hz=hz, lv=lv, ct=ct, rd=rd, rp=rp,
                        ppe=[x.strip() for x in ppe.split(";") if x.strip()], mo=mo, st=st))
    return out


def _tools(text):
    return [(ph, cat, tags.split(";")) for ph, cat, tags in (ln.split("|") for ln in text.strip().splitlines())]


def _table(ws, name, headers, rows, widths, wrap_cols=()):
    ws.append(headers)
    for c in ws[1]:
        c.fill, c.font, c.alignment = HDR_FILL, HDR_FONT, Alignment(vertical="center", wrap_text=True)
    for r in rows:
        ws.append(r)
    last = 1 + max(len(rows), 1)
    for row in ws.iter_rows(min_row=2, max_row=last, max_col=len(headers)):
        for cell in row:
            cell.font = BODY
            cell.alignment = WRAP if cell.column in wrap_cols else TOP
    t = Table(displayName=name, ref=f"A1:{ws.cell(row=last, column=len(headers)).column_letter}{last}")
    t.tableStyleInfo = TableStyleInfo(name="TableStyleLight9", showRowStripes=True)
    ws.add_table(t)
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[ws.cell(row=1, column=i).column_letter].width = w
    ws.freeze_panes = "A2"
    return last


def _dv(ws, formula, cols, last, msg):
    dv = DataValidation(type="list", formula1=formula, allow_blank=True, showErrorMessage=True, errorTitle="Not in list", error=msg)
    for col in cols:
        dv.add(f"{col}2:{col}{last + 300}")
    ws.add_data_validation(dv)


def build(bu: str, outpath: str | Path) -> Path:
    m = importlib.import_module(SOURCES[bu])
    P = m.ID_PREFIX
    tags = [(c, t) for c, ts in m.COMMON_TAGS for t in ts] + [(c, t) for c, ts in m.BU_TAGS for t in ts]
    tagset = [t for _, t in tags]
    ah = _rows(m.COMMON_AH) + _rows(m.BU_AH)
    eh = _rows(m.EH)
    tools = _tools(m.COMMON_TOOLS) + _tools(m.TOOLS)
    rules = list(m.COMMON_RULES) + list(m.RULES)
    syns = [ln.split("|") for ln in m.SYNONYMS.strip().splitlines()]
    locs, types = m.LOCATIONS, m.EQUIPMENT_TYPES
    locnames, loctype = [l for l, _ in locs], dict(locs)

    # ---- integrity checks: refuse to build a broken default ----
    errs = []
    if len(tagset) != len(set(tagset)):
        errs.append("duplicate activities")
    errs += [f"hazard for unknown activity {h['key']}" for h in ah if h["key"] not in tagset]
    errs += [f"hazard for unknown equipment type {h['key']}" for h in eh if h["key"] not in types]
    errs += [f"activity without hazard: {t}" for t in tagset if t not in {h['key'] for h in ah}]
    errs += [f"equipment type without hazard: {t}" for t in types if t not in {h['key'] for h in eh}]
    eqmap = {n: (t, sc, ar) for n, t, sc, ar in m.EQUIPMENT}
    for n, (t, sc, ar) in eqmap.items():
        errs += [f"{n}: unknown type"] if t not in types else []
        errs += [f"{n}: unknown area {a}" for a in ar if a not in locnames]
    for ph, _, tg in tools:
        errs += [f"tool {ph}: unknown activity {t}" for t in tg if t not in tagset]
    for r in rules:
        errs += [f"rule {r[2]}: unknown activity {t}" for t in r[3] if t not in tagset]
    errs += [f"synonym {ph}: unknown activity {t}" for ph, t in syns if t not in tagset]
    for n, c, d, pt, et, mo, st, ref, loc in m.PRESETS:
        errs += [f"preset {n}: unknown activity {t}" for t in pt if t not in tagset]
        if ref not in eqmap or eqmap[ref][0] != et:
            errs.append(f"preset {n}: equipment/type mismatch")
        elif loc:
            t_, sc, ar = eqmap[ref]
            if not (sc == "All areas" or (sc == "All process areas" and loctype.get(loc) == "Process") or loc in ar):
                errs.append(f"preset {n}: {ref} not available in {loc}")
    errs += [f"bad risk level: {h['hz']}" for h in ah + eh if h["lv"] not in "EHMLN" or h["rd"] not in "EHMLN"]
    if errs:
        raise ValueError(f"{bu} default register failed checks:\n" + "\n".join(errs))

    resp = sorted(set(m.COMMON_RESP + m.RESP + [h["rp"] for h in ah + eh]))
    ppe = sorted({p for h in ah + eh for p in h["ppe"]})
    cats = list(dict.fromkeys(c for c, _ in tags))
    pcats = list(dict.fromkeys(p[1] for p in m.PRESETS))
    tcats = sorted({t[1] for t in tools})

    wb = Workbook()
    ws = wb.active
    ws.title = "ReadMe"
    readme = [
        (m.BU["title"], TITLE), ("", BODY),
        ("STATUS: DRAFT v1 — built-in default register. Every hazard, control, risk level and responsible role MUST be reviewed", Font(name="Arial", bold=True, color="C6303E")),
        ("and approved by the business unit HSE lead before the register is used for live work.", Font(name="Arial", bold=True, color="C6303E")), ("", BODY),
        ("OWNERSHIP", SECTION),
        ("This workbook is the ONLY source the app uses for this business unit. It does not share rows with any other business unit's", BODY),
        (f"register. Edits here affect this business unit only. All row IDs carry the prefix '{P}-'.", BODY), ("", BODY),
        ("HOW TO UPDATE", SECTION),
        ("1. In the app, open the Register admin tab, select this business unit and download the current register.", BODY),
        ("2. Edit it in Excel. Every controlled column has a dropdown; add new options beneath the relevant list on the Lists sheet.", BODY),
        ("3. Do not rename sheets or column headers - the app matches on these names.", BODY),
        ("4. Upload the edited file on the Register admin tab. The app checks it, shows what changed, and activates it only when you confirm.", BODY),
        ("", BODY), ("SHEETS", SECTION),
        ("Settings           Banner text, register status and Emergency Response Plan lines printed on every PDF.", BODY),
        ("Lists              Dropdown source lists (categories, risk levels, PPE, responsible persons, motion/status options).", BODY),
        ("Locations          Plant areas. GENERIC layout - rename and recode to the site's real unit numbers.", BODY),
        ("JobTags            Work activities.   EquipmentTypes  Equipment categories.   Equipment  Specific items + where they are found.", BODY),
        ("ActivityHazards    Hazards driven by the activity.   EquipmentHazards  Hazards driven by the equipment type.", BODY),
        ("TaskPresets        One-tap jobs.   ToolRecognition  Tool phrases.   InferenceRules  Description rules.   Synonyms  Description words.", BODY),
    ]
    for i, (line, font) in enumerate(readme, 1):
        ws.cell(row=i, column=1, value=line).font = font
    ws.column_dimensions["A"].width = 130

    ws = wb.create_sheet("Settings")
    st_rows = [["BusinessUnit", m.BU["unit"]], ["CompanyName", m.BU["company"]], ["FormTitle", "RISK ASSESSMENT FORM"],
               ["RegisterStatus", "DRAFT v1 - pending HSE validation"]] + [[f"ERP{i}", x] for i, x in enumerate(m.ERP, 1)]
    _table(ws, "tblSettings", ["Key", "Value"], st_rows, [22, 110], wrap_cols=(2,))

    ws = wb.create_sheet("Lists")
    ws["A1"] = "MASTER DROPDOWN LISTS — add a new option in the first blank cell directly beneath any list."
    ws["A1"].font = NOTE
    lists = [("Category", cats), ("HazardCategory", list(CAT.values())), ("RiskLevel", list("EHMLN")), ("ResponsiblePerson", resp),
             ("PPEItem", ppe), ("MotionOption", ["Any", "Running", "Static"]), ("StatusOption", ["Any", "Operational", "Shutdown/Isolated"]),
             ("PresetCategory", pcats), ("ToolCategory", tcats), ("AreaType", ["Process", "Utility", "Site", "Building", "Other"]),
             ("LocationScope", ["Listed areas only", "All process areas", "All areas"])]
    for ci, (hdr, vals) in enumerate(lists, 1):
        cell = ws.cell(row=2, column=ci, value=hdr)
        cell.fill, cell.font = HDR_FILL, HDR_FONT
        for ri, v in enumerate(vals, 3):
            ws.cell(row=ri, column=ci, value=v).font = BODY
        col = cell.column_letter
        ws.column_dimensions[col].width = max(16, min(40, max(len(str(v)) for v in vals + [hdr]) + 2))
        wb.defined_names[f"lst{hdr}"] = DefinedName(f"lst{hdr}", attr_text=f"OFFSET(Lists!${col}$3,0,0,MAX(1,COUNTA(Lists!${col}$3:${col}$2000)),1)")
    ws.freeze_panes = "A3"
    L = {h: f"=lst{h}" for h, _ in lists}

    def named(name, sheet, col, n=3000):
        wb.defined_names[name] = DefinedName(name, attr_text=f"OFFSET({sheet}!${col}$2,0,0,MAX(1,COUNTA({sheet}!${col}$2:${col}${n})),1)")

    ws = wb.create_sheet("Locations")
    last = _table(ws, "tblLocations", ["LocationID", "LocationCode", "LocationArea", "AreaType", "AddedByReview"],
                  [[f"{P}-LOC{i:02d}", "", n, t, ""] for i, (n, t) in enumerate(locs, 1)], [14, 14, 46, 12, 15])
    _dv(ws, L["AreaType"], ["D"], last, "Choose an AreaType from the Lists sheet.")
    named("lstLocationArea", "Locations", "C")

    ws = wb.create_sheet("JobTags")
    last = _table(ws, "tblJobTags", ["JobTagID", "JobTag", "Category"], [[f"{P}-TAG{i:03d}", t, c] for i, (c, t) in enumerate(tags, 1)], [14, 46, 28])
    _dv(ws, L["Category"], ["C"], last, "Choose a Category from the Lists sheet.")
    named("lstJobTag", "JobTags", "B")

    ws = wb.create_sheet("EquipmentTypes")
    _table(ws, "tblEquipmentTypes", ["EquipmentTypeID", "EquipmentType"], [[f"{P}-ET{i:02d}", t] for i, t in enumerate(types, 1)], [16, 48])
    named("lstEquipmentType", "EquipmentTypes", "B")

    ws = wb.create_sheet("Equipment")
    last = _table(ws, "tblEquipment", ["EquipmentID", "EquipmentName", "EquipmentType", "LocationScope"] + [f"LocationArea{i}" for i in range(1, 11)],
                  [[f"{P}-EQ{i:02d}", n, t, sc] + (ar + [""] * 10)[:10] for i, (n, t, sc, ar) in enumerate(m.EQUIPMENT, 1)], [13, 36, 34, 18] + [30] * 10)
    _dv(ws, "=lstEquipmentType", ["C"], last, "Choose an EquipmentType.")
    _dv(ws, L["LocationScope"], ["D"], last, "Choose a LocationScope.")
    _dv(ws, "=lstLocationArea", list("EFGHIJKLMN"), last, "Choose a LocationArea from the Locations sheet.")
    named("lstEquipmentName", "Equipment", "B")

    for sheet, keycol, pre, lst, tname, keydv in (("ActivityHazards", "JobTag", "AH", ah, "tblActivityHazards", "=lstJobTag"),
                                                  ("EquipmentHazards", "EquipmentType", "EH", eh, "tblEquipmentHazards", "=lstEquipmentType")):
        ws = wb.create_sheet(sheet)
        hdr = [f"{sheet[:-1]}ID", keycol, "HazardCategory", "Hazard", "LevelOfRisk", "ControlMeasures", "ReducedLevelOfRisk", "ResponsiblePerson"] + \
              [f"PPE{i}" for i in range(1, 8)] + ["AppliesWhenMotion", "AppliesWhenStatus"]
        rows = [[f"{P}-{pre}{i:03d}", h["key"], h["cat"], h["hz"], h["lv"], h["ct"], h["rd"], h["rp"]] + (h["ppe"] + [""] * 7)[:7] + [h["mo"], h["st"]]
                for i, h in enumerate(lst, 1)]
        last = _table(ws, tname, hdr, rows, [13, 34, 26, 50, 10, 70, 12, 30] + [22] * 7 + [14, 18], wrap_cols=(4, 6))
        _dv(ws, keydv, ["B"], last, f"Choose a {keycol} that exists in the register.")
        _dv(ws, L["HazardCategory"], ["C"], last, "Choose a HazardCategory.")
        _dv(ws, L["RiskLevel"], ["E", "G"], last, "Risk level must be E, H, M, L or N.")
        _dv(ws, L["ResponsiblePerson"], ["H"], last, "Choose a ResponsiblePerson from the Lists sheet.")
        _dv(ws, L["PPEItem"], list("IJKLMNO"), last, "Choose a PPE item from the Lists sheet.")
        _dv(ws, L["MotionOption"], ["P"], last, "Choose from MotionOption.")
        _dv(ws, L["StatusOption"], ["Q"], last, "Choose from StatusOption.")

    ws = wb.create_sheet("TaskPresets")
    hdr = ["PresetID", "PresetName", "PresetCategory", "Description"] + [f"JobTag{i}" for i in range(1, 11)] + \
          ["EquipmentType", "EquipmentMotion", "EquipmentStatus", "EquipmentRef", "LocationArea"]
    last = _table(ws, "tblTaskPresets", hdr, [[f"{P}-P{i:02d}", n, c, d] + (t + [""] * 10)[:10] + [et, mo, st, ref, loc]
                                             for i, (n, c, d, t, et, mo, st, ref, loc) in enumerate(m.PRESETS, 1)],
                  [11, 32, 16, 50] + [28] * 10 + [32, 15, 17, 32, 34], wrap_cols=(4,))
    _dv(ws, L["PresetCategory"], ["C"], last, "Choose a PresetCategory.")
    _dv(ws, "=lstJobTag", [ws.cell(row=1, column=c).column_letter for c in range(5, 15)], last, "Choose a JobTag.")
    _dv(ws, "=lstEquipmentType", ["O"], last, "Choose an EquipmentType.")
    _dv(ws, "=lstEquipmentName", ["R"], last, "Choose equipment from the Equipment sheet.")
    _dv(ws, "=lstLocationArea", ["S"], last, "Choose a LocationArea (or leave blank).")

    ws = wb.create_sheet("ToolRecognition")
    last = _table(ws, "tblToolRecognition", ["ToolID", "ToolPhrase", "ToolCategory"] + [f"JobTag{i}" for i in range(1, 6)],
                  [[f"{P}-T{i:03d}", ph, c] + (tg + [""] * 5)[:5] for i, (ph, c, tg) in enumerate(tools, 1)], [12, 22, 20] + [34] * 5)
    _dv(ws, L["ToolCategory"], ["C"], last, "Choose a ToolCategory.")
    _dv(ws, "=lstJobTag", list("DEFGH"), last, "Choose a JobTag.")

    ws = wb.create_sheet("InferenceRules")
    last = _table(ws, "tblInferenceRules", ["RuleID", "TriggerRegex", "AlsoRequiresRegex", "Label", "JobTag1", "JobTag2", "JobTag3"],
                  [[f"{P}-IR{i:02d}", a, b, c] + (d + ["", "", ""])[:3] for i, (a, b, c, d) in enumerate(rules, 1)], [11, 70, 60, 26, 34, 34, 34], wrap_cols=(2, 3))
    _dv(ws, "=lstJobTag", list("EFG"), last, "Choose a JobTag.")

    ws = wb.create_sheet("Synonyms")
    last = _table(ws, "tblSynonyms", ["SynonymID", "Phrase", "JobTag"], [[f"{P}-S{i:03d}", ph, t] for i, (ph, t) in enumerate(syns, 1)], [14, 26, 46])
    _dv(ws, "=lstJobTag", ["C"], last, "Choose a JobTag.")

    outpath = Path(outpath)
    outpath.parent.mkdir(parents=True, exist_ok=True)
    tmp = outpath.with_suffix(".tmp.xlsx")
    wb.save(tmp)
    tmp.replace(outpath)
    return outpath


if __name__ == "__main__":
    out = Path(sys.argv[1] if len(sys.argv) > 1 else "registers")
    for bu in SOURCES:
        m = importlib.import_module(SOURCES[bu])
        print(build(bu, out / m.BU["file"]))
