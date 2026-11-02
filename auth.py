"""Sign-in: username/password (test account until real users are added to Secrets), or Microsoft sign-in if configured.

Secrets examples (.streamlit/secrets.toml or Streamlit Cloud > Settings > Secrets):

    [users.jakukuata]
    name = "John Akukuata"
    password_hash = "pbkdf2_sha256$200000$<salt>$<hash>"     # from make_password_hash.py

    # Optional Microsoft sign-in (st.login) - replaces passwords when present
    [auth]
    redirect_uri = "https://<your-app>.streamlit.app/oauth2callback"
    cookie_secret = "<random string>"
    client_id = "<entra app id>"
    client_secret = "<entra secret>"
    server_metadata_url = "https://login.microsoftonline.com/<tenant-id>/v2.0/.well-known/openid-configuration"
    allowed_domain = "dangote.com"

    # Switch sign-in off completely (local testing only)
    [app]
    require_sign_in = false
"""
from __future__ import annotations

import hashlib
import hmac
import secrets as _secrets
import time

import streamlit as st

TEST_USER = "okpella.test"
TEST_NAME = "Test User"
MAX_TRIES, LOCK_SECONDS, ITERS = 5, 60, 200_000


def hash_password(pw: str, salt: str | None = None, iters: int = ITERS) -> str:
    salt = salt or _secrets.token_hex(16)
    dk = hashlib.pbkdf2_hmac("sha256", pw.encode(), bytes.fromhex(salt), iters)
    return f"pbkdf2_sha256${iters}${salt}${dk.hex()}"


def verify(pw: str, stored: str) -> bool:
    try:
        algo, iters, salt, _ = stored.split("$")
        return algo == "pbkdf2_sha256" and hmac.compare_digest(hash_password(pw, salt, int(iters)), stored)
    except Exception:
        return False


def _secret(section: str) -> dict:
    try:
        return dict(st.secrets.get(section, {}))
    except Exception:
        return {}


def _users() -> dict:
    return {k.lower(): dict(v) for k, v in _secret("users").items()}


def test_account_active() -> bool:
    return not _users()


@st.cache_resource
def _attempts() -> dict:
    return {}   # shared across sessions on this server: username -> [fails, locked_until]


def _oidc_configured() -> bool:
    a = _secret("auth")
    return bool(a.get("client_id") and a.get("redirect_uri") and a.get("cookie_secret"))


def current_user() -> dict | None:
    return st.session_state.get("user")


def sign_out():
    st.session_state.pop("user", None)
    if _oidc_configured():
        try:
            st.logout()
        except Exception:
            pass


def require_sign_in(render_header) -> dict:
    """Returns the signed-in user, or renders the sign-in page and stops the script."""
    if not _secret("app").get("require_sign_in", True):
        st.session_state.setdefault("user", {"username": "local", "name": ""})
        return st.session_state["user"]
    if "user" in st.session_state:
        return st.session_state["user"]

    if _oidc_configured():
        u = getattr(st, "user", None)
        logged = bool(getattr(u, "is_logged_in", False)) if u is not None else False
        if logged:
            email = str(u.get("email", "") or "")
            dom = _secret("auth").get("allowed_domain", "")
            if dom and not email.lower().endswith("@" + dom.lower()):
                render_header()
                st.error(f"Only @{dom} accounts can use this app.")
                if st.button("Sign out"):
                    st.logout()
                st.stop()
            st.session_state["user"] = {"username": email, "name": str(u.get("name", "") or email)}
            return st.session_state["user"]
        render_header()
        with st.container(border=True):
            st.markdown("### Sign in")
            st.caption("Use your company Microsoft account.")
            if st.button("Sign in with Microsoft", type="primary", width="stretch"):
                st.login()
        st.stop()

    render_header()
    with st.container(border=True):
        st.markdown("### Sign in")
        if test_account_active():
            st.warning(f"**Test sign-in is active.** Username `{TEST_USER}` · password `Okpella@Test2026`. "
                       "It switches off automatically once real users are added to Secrets.")
        with st.form("signin"):
            un = st.text_input("Username").strip().lower()
            pw = st.text_input("Password", type="password")
            go = st.form_submit_button("Sign in", type="primary", width="stretch")
        if go:
            att = _attempts()
            fails, until = att.get(un, [0, 0.0])
            if time.time() < until:
                st.error(f"Too many attempts. Try again in {int(until - time.time()) + 1} s.")
                st.stop()
            ok, name = False, ""
            if test_account_active():
                ok, name = (un == TEST_USER and pw == "Okpella@Test2026"), TEST_NAME
            else:
                rec = _users().get(un)
                if rec and verify(pw, rec.get("password_hash", "")):
                    ok, name = True, rec.get("name", un)
            if ok:
                att.pop(un, None)
                st.session_state["user"] = {"username": un, "name": name}
                st.rerun()
            fails += 1
            att[un] = [fails, time.time() + LOCK_SECONDS if fails >= MAX_TRIES else 0.0]
            if fails >= MAX_TRIES:
                att[un] = [0, time.time() + LOCK_SECONDS]
                st.error(f"Too many attempts. Sign-in is blocked for {LOCK_SECONDS} seconds.")
            else:
                st.error("Incorrect username or password.")
    st.stop()
