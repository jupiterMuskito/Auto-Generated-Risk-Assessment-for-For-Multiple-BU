"""Colour scheme and typography from the original OKPELLA HTML app (deep blue app bar, red accent, Oswald/Inter)."""
import html

import streamlit as st

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@500;600&display=swap');
:root{
  --bg:#eef3fa; --surface-2:#e4eefb; --paper:#ffffff; --paper-dim:#f2f6fc;
  --ink:#14202e; --ink-dim:#5c7086; --line:#d7e3ee;
  --blue-deep:#123a73; --blue:#1d63c4; --blue-dark:#0f4694; --blue-light:#e4eefb;
  --red:#c6303e; --red-dark:#a2242f;
  --e:#c6303e; --h:#e0793a; --m:#d9b23a; --l:#4f9d63; --n:#4a7fc9;
}
html, body, .stApp, [class*="css"]{font-family:'Inter',system-ui,sans-serif;}
.stApp{background:var(--bg); color:var(--ink);}
.block-container{max-width:780px; padding-top:1rem; padding-bottom:5rem;}
h1,h2,h3{font-family:'Oswald',sans-serif !important; text-transform:uppercase; letter-spacing:.04em; color:var(--blue-deep);}
h3{font-size:1.05rem !important;}
header[data-testid="stHeader"]{background:transparent;}
.appbar{background:var(--blue-deep); border-bottom:3px solid var(--red); border-radius:10px; padding:13px 16px 11px; margin-bottom:14px;}
.appbar h1{color:#fff !important; font-size:20px !important; margin:0 0 2px; padding:0; font-weight:700;}
.appbar .sub{color:#bcd2ee; font-size:12px; margin:0;}
.appbar .bu{display:inline-block; margin-top:6px; background:rgba(255,255,255,.12); color:#fff; border:1px solid rgba(255,255,255,.3);
  border-radius:14px; padding:2px 10px; font-size:11.5px; font-family:'IBM Plex Mono',monospace;}
[data-testid="stVerticalBlockBorderWrapper"]{background:var(--paper); border-radius:10px !important; border-color:var(--line) !important; box-shadow:0 1px 2px rgba(0,0,0,.08);}
.stButton>button, .stDownloadButton>button, .stFormSubmitButton>button{font-family:'Oswald',sans-serif; text-transform:uppercase; letter-spacing:.04em; font-weight:600; border-radius:8px;}
.stButton>button[kind="primary"], .stDownloadButton>button[kind="primary"], .stFormSubmitButton>button[kind="primary"]{background:var(--blue); border-color:var(--blue);}
.stButton>button[kind="primary"]:hover, .stDownloadButton>button[kind="primary"]:hover{background:var(--blue-dark); border-color:var(--blue-dark);}
.stButton>button[kind="secondary"]{background:var(--blue-light); color:var(--blue-deep); border-color:var(--line);}
.stTabs [data-baseweb="tab-list"]{background:var(--surface-2); border-radius:8px 8px 0 0; gap:0;}
.stTabs [data-baseweb="tab"]{font-family:'Oswald',sans-serif; text-transform:uppercase; letter-spacing:.03em; color:var(--ink-dim); flex:1; justify-content:center;}
.stTabs [aria-selected="true"]{color:var(--blue-deep) !important;}
.stTabs [data-baseweb="tab-highlight"]{background:var(--red) !important;}
label p{font-size:12px !important; font-weight:600 !important; color:var(--ink-dim) !important; text-transform:uppercase; letter-spacing:.03em;}
.report-banner{background:var(--blue-deep); color:#fff; padding:16px; border-radius:10px 10px 0 0; text-align:center; border-bottom:3px solid var(--red);}
.report-banner .company{font-family:'Oswald',sans-serif; font-size:17px; font-weight:700; letter-spacing:.04em;}
.report-banner .form-title{font-size:12.5px; color:#bcd2ee; margin-top:2px; letter-spacing:.06em;}
.kv{display:flex; justify-content:space-between; gap:10px; padding:6px 0; border-bottom:1px solid var(--paper-dim); font-size:13px;}
.kv .k{color:var(--ink-dim); font-weight:600; width:38%; flex:none;} .kv .v{text-align:right; flex:1; font-weight:500;}
.strip{display:flex; gap:6px; margin:12px 0; flex-wrap:wrap;}
.chip{font-family:'IBM Plex Mono',monospace; font-size:11px; font-weight:600; color:#fff; padding:5px 10px; border-radius:20px;}
.chip.E{background:var(--e);} .chip.H{background:var(--h);} .chip.M{background:var(--m); color:#3a2f00;}
.chip.L{background:var(--l);} .chip.N{background:var(--n);} .chip.total{background:var(--blue-deep);} .chip.X{background:#8c98a4;}
.sec{font-family:'Oswald',sans-serif; text-transform:uppercase; letter-spacing:.04em; font-size:13px; background:var(--blue-deep); color:#fff; padding:8px 10px; border-radius:6px; margin:16px 0 8px;}
.hcard{border:1px solid var(--line); border-radius:8px; padding:9px 12px; margin:-6px 0 10px; background:#fff;}
.hcard .top{display:flex; justify-content:space-between; gap:8px;}
.hcard .t{font-size:13.5px; font-weight:600; line-height:1.35;}
.hcard .c{font-size:12.5px; color:var(--ink-dim); line-height:1.45; margin-top:4px;}
.hcard .r{font-size:11px; color:var(--ink-dim); margin:5px 0;}
.hcard .s{font-size:10px; color:#8b99a8; font-family:'IBM Plex Mono',monospace;}
.badge{font-family:'IBM Plex Mono',monospace; font-size:11px; font-weight:700; color:#fff; border-radius:5px; padding:2px 7px; flex:none; height:fit-content;}
.badge.E{background:var(--e);} .badge.H{background:var(--h);} .badge.M{background:var(--m); color:#3a2f00;} .badge.L{background:var(--l);} .badge.N{background:var(--n);}
.hcard.x{background:repeating-linear-gradient(135deg,#f6f7f9 0 10px,#eceff3 10px 20px); border-color:#c9d2db;}
.hcard.x .t{text-decoration:line-through; color:#7d8996;} .hcard.x .c,.hcard.x .r,.hcard.x .s{color:#98a3ae;} .hcard.x .badge{opacity:.45; filter:grayscale(.75);}
.xtag{display:inline-block; margin-top:6px; font-family:'IBM Plex Mono',monospace; font-size:9.5px; color:#5f6b77; background:#e6eaee; border:1px dashed #aab5c0; border-radius:4px; padding:3px 8px;}
.verify{background:#fff8e6; border:1px solid #f0d9a0; border-left:4px solid #d9a441; border-radius:8px; padding:10px 12px; margin:12px 0; font-size:12.5px; line-height:1.5;}
.verify b{color:#8a6414;}
.ppe{font-size:12.5px; line-height:1.6; background:var(--paper-dim); padding:10px 12px; border-radius:6px;}
.erp{background:var(--blue-light); border:1px solid var(--line); border-left:4px solid var(--red); border-radius:8px; padding:10px 12px; font-size:12.5px; line-height:1.6; margin-top:14px;}
.erp strong{display:block; margin-bottom:4px; color:var(--red-dark);}
.valbanner{background:#fbe9e7; border:1px solid #f0b3ad; border-left:4px solid var(--red); border-radius:8px; padding:10px 12px; margin:6px 0 10px; font-size:12.5px; color:#8a2a22;}
.noreg{background:#fbe9e7; border:1px solid #f0b3ad; border-left:5px solid var(--red); border-radius:8px; padding:14px 16px; margin:8px 0 12px; color:#8a2a22;}
.noreg h4{font-family:'Oswald',sans-serif; text-transform:uppercase; color:var(--red-dark); margin:0 0 6px; letter-spacing:.04em;}
.okbox{background:#e9f5ec; border:1px solid #b9dcc3; border-left:4px solid #4f9d63; border-radius:8px; padding:10px 12px; margin:6px 0 10px; font-size:12.5px; color:#1f5130;}
.hint{font-size:12px; color:var(--ink-dim); margin:-4px 0 10px; line-height:1.45;}
.bu-card{border:1.5px solid var(--line); border-radius:9px; padding:10px 13px; background:#fff; margin-bottom:6px;}
.bu-card .n{font-weight:700; font-size:13.5px;} .bu-card .d{font-size:11.5px; color:var(--ink-dim); margin-top:2px;}
.ok{color:#1f6b3a; font-weight:600;} .bad{color:var(--red-dark); font-weight:600;}
.src-pill{display:inline-block; font-family:'IBM Plex Mono',monospace; font-size:10.5px; padding:1px 8px; border-radius:10px; background:var(--blue-light); color:var(--blue-deep); border:1px solid var(--line);}
section[data-testid="stSidebar"]{background:var(--surface-2);}
</style>
"""


def apply():
    st.markdown(CSS, unsafe_allow_html=True)


def appbar(bu_name: str | None = None):
    bu = f'<div class="bu">{html.escape(bu_name)}</div>' if bu_name else ""
    st.markdown(f'<div class="appbar"><h1>Risk Assessment Generator</h1><p class="sub">Dangote Group — multi-business-unit edition</p>{bu}</div>',
                unsafe_allow_html=True)
