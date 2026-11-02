# Risk Assessment Generator — v5.3 (multi-business-unit)

Sign in → select business unit → **Build** (job → hazards → review → PDF) · **Register** (view) · **Admin** (password-protected, same layout as the original HTML app).
Each business unit uses only its own register workbook. Nothing is shared between business units.

## Admin page (v5.3 — ported from the original HTML app)
- **Admin Access** lock: admin password (default `OkpellaAdmin@2026`; change it on the page, or set `[admin] password_hash` in Secrets via `python make_password_hash.py --admin`).
- **Manage Data**: upload an updated workbook (loaded immediately with a status message), current-data summary, Download Master Workbook, Restore built-in default. Applies to the selected business unit only; a workbook whose Settings sheet names another business unit is refused.
- **Assessment Log**: summary, 60 most recent entries, Export CSV / JSON, Clear log with confirmation. Same columns as the HTML app plus businessUnit and registerFingerprint. Filter by this business unit or all.
- **Admin password**: change it on this server.
Not ported: the LLM API key box and JSON config import/export (the Streamlit app has no LLM mode and uses the Excel workbook as its only data source).

## Earlier changes (v5.2)
| Change | Detail |
|---|---|
| Built-in default registers | Refinery and fertiliser registers ship with the app in `registers/`. If those files are missing from the repo, the app recreates them automatically from each BU's own source file in `ra/defaults/` (identical content and fingerprint). |
| BUs without a register | Sugar, NASCON and Packaging show the "Risk register update required" report until a register is uploaded for them on the Admin page. |

## Deploy (keep the folders!)
Replace the repo contents with this package, keeping the folder structure:
```
app.py  bu_config.json  requirements.txt  make_password_hash.py  README.md
.streamlit/config.toml
registers/DANGOTE_REFINERY_Master_Workbook_v1.xlsx
registers/DANGOTE_FERTILISER_Master_Workbook_v1.xlsx
ra/__init__.py  ra/auth.py  ra/engine.py  ra/pdf_report.py  ra/store.py  ra/theme.py
ra/defaults/__init__.py  ra/defaults/build.py  ra/defaults/refinery.py  ra/defaults/fertiliser.py
data/.gitkeep
```
Then **Manage app → Reboot app**.

## Cement register
Open the app → Dangote Cement → **Admin** → unlock → upload `OKPELLA_Master_Workbook_v8.xlsx` (with the Settings and Synonyms sheets from the add-on if you have added them).
For it to survive restarts, also commit it to `registers/OKPELLA_Master_Workbook_v8.xlsx` (or set up the GitHub option below so the app does this for you).

## Making uploads permanent (important on Streamlit Community Cloud)
Streamlit Cloud deletes uploaded files whenever the app restarts or is redeployed; the app then falls back to the built-in default.
Two ways to keep an upload:
1. **Automatic (recommended):** create a GitHub *fine-grained personal access token* limited to this repo with **Contents: Read and write**, then add to Secrets:
   ```toml
   [github]
   token = "github_pat_..."
   repo = "your-username/your-repo-name"
   branch = "main"
   ```
   Every upload is then also committed to the BU's path in `registers/` and becomes the new built-in default.
2. **Manual:** after uploading, use "Download Master Workbook" and commit that file to `registers/` with the file name shown in `bu_config.json`.

## Users
For each person run `python make_password_hash.py` and paste the block into **Settings → Secrets**. Once any user is added the test account stops working. Five wrong passwords lock that username for 60 seconds.

## Before live use of the refinery and fertiliser registers
They are **draft** registers: the BU HSE lead must review every row, rename the generic locations to the real unit names, and replace the
`[TO BE CONFIRMED]` emergency numbers on the Settings sheet. Every PDF from a DRAFT register carries a visible warning.
