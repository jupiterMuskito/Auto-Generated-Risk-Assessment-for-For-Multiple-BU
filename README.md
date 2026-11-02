# Risk Assessment Generator — v5 (multi-business-unit)

Streamlit app. The user signs in, **selects the business unit first**, builds the job, reviews the hazards, then downloads the PDF.
Every hazard, control, risk level, responsible person and PPE item is copied from the selected business unit's register workbook.

## What changed in v5
| Change | Detail |
|---|---|
| Business-unit selection | First screen after sign-in. Business units are listed in `bu_config.json`. |
| Cement | Uses the existing **OKPELLA_Master_Workbook_v8.xlsx** (unchanged). |
| Refinery | New register: `registers/DANGOTE_REFINERY_Master_Workbook_v1.xlsx` (DRAFT). |
| Fertiliser | New register: `registers/DANGOTE_FERTILISER_Master_Workbook_v1.xlsx` (DRAFT). |
| BUs without a register | Sugar, NASCON and Packaging are listed. Selecting one shows a **"Risk register update required"** report with a downloadable request PDF and a blank register template. The same report appears automatically if a linked file is missing or unreadable. |
| Colour scheme | Restored to the original HTML app: deep-blue app bar `#123a73` with red `#c6303e` accent, blue `#1d63c4` buttons, `#eef3fa` page, E/H/M/L/N badge colours, Oswald/Inter type. The PDF uses the same palette. |

## Setup
1. **Copy your cement register into the app:** put `OKPELLA_Master_Workbook_v8.xlsx` in the `registers/` folder.
   It is not included in this package. Until it is there, Cement shows the "register update required" report.
2. Deploy as before (GitHub repo → Streamlit Community Cloud → main file `app.py`).
3. Sign-in: the test account `okpella.test` / `Okpella@Test2026` works until real users are added.
   For each real user run `python make_password_hash.py` and paste the block into **Settings → Secrets**.
   Five wrong passwords lock that username for 60 seconds. Microsoft sign-in can be switched on in Secrets (see `ra/auth.py`).

## Adding another business unit later
1. Fill in the blank template (downloadable from the app when that BU is selected). Keep the same sheet and column names as the Okpella workbook.
2. Put the workbook in `registers/` and set its path in the `register` field for that BU in `bu_config.json`.
3. Optional `Settings` sheet in the workbook: `CompanyName`, `FormTitle`, `RegisterStatus`, `ERP1`–`ERP3` (these override `bu_config.json`).

## Before live use of the refinery and fertiliser registers
- They are **draft starting registers**, not approved registers. The BU HSE lead must review every row.
- **Locations are a generic unit layout.** Rename and recode them to the site's real unit numbers.
- **Emergency numbers are placeholders** (`[TO BE CONFIRMED]`) on each workbook's `Settings` sheet.
- Every PDF from a register marked DRAFT carries a visible draft warning.

## Files
`app.py` (UI) · `ra/engine.py` (register loader, hazard engine, description helper, serial number) · `ra/pdf_report.py` (PDF and request notice) ·
`ra/auth.py` (sign-in) · `ra/theme.py` (colour scheme) · `bu_config.json` · `registers/` · `data/` (assessment log CSV, resets on Streamlit Cloud restarts).
