"""Sign-in and roles.

Secrets (.streamlit/secrets.toml locally, or Streamlit Cloud > Manage app > Settings > Secrets):

    [users.jakukuata]
    name = "John Akukuata"
    password_hash = "pbkdf2_sha256$200000$<salt>$<hash>"     # from: python make_password_hash.py

    [users.operator1]
    name = "Shift Operator"
    password_hash = "..."

    # Optional Microsoft sign-in (st.login) - replaces passwords when present
    [auth]
    redirect_uri = "https://<your-app>.streamlit.app/oauth2callback"
    cookie_secret = "<random string>"
    client_id = "<entra app id>"
    client_secret = "<entra secret>"
    server_metadata_url = "https://login.microsoftonline.com/<tenant-id>/v2.0/.well-known/openid-configuration"
    allowed_domain = "dangote.com"

    [admin]
    password_hash = "pbkdf2_sha256$..."      # admin-page password (python make_password_hash.py --admin)

While no [users] are configured, the published TEST account is active.
"""
from __future__ import annotations

import hashlib
import hmac
import secrets as _secrets
import time

import streamlit as st

TEST_USER, TEST_PASS, TEST_NAME = "okpella.test", "Okpella@Test2026", "Test User"
MAX_TRIES, LOCK_SECONDS, ITERS = 5, 60, 200_000


def hash_password(pw: str, salt: str | None = None, iters: int = ITERS) -> str:
    salt = salt or _secrets.token_hex(16)
    return f"pbkdf2_sha256${iters}${salt}${hashlib.pbkdf2_hmac('sha256', pw.encode(), bytes.fromhex(salt), iters).hex()}"


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


def _oidc_configured() -> bool:
    a = _secret("auth")
    return bool(a.get("client_id") and a.get("redirect_uri") and a.get("cookie_secret"))


@st.cache_resource
def _attempts() -> dict:
    return {}


def is_admin(user: dict | None) -> bool:
    return bool(user and user.get("role") == "admin")


def sign_out():
    st.session_state.pop("user", None)
    if _oidc_configured():
        try:
            st.logout()
        except Exception:
            pass


def require_sign_in(render_header) -> dict:
    if not _secret("app").get("require_sign_in", True):
        st.session_state.setdefault("user", {"username": "local", "name": "", "role": "admin"})
        return st.session_state["user"]
    if "user" in st.session_state:
        return st.session_state["user"]

    if _oidc_configured():
        u = getattr(st, "user", None)
        if u is not None and getattr(u, "is_logged_in", False):
            email = str(u.get("email", "") or "")
            dom = _secret("auth").get("allowed_domain", "")
            if dom and not email.lower().endswith("@" + dom.lower()):
                render_header()
                st.error(f"Only @{dom} accounts can use this app.")
                st.button("Sign out", on_click=st.logout)
                st.stop()
            admins = [a.lower() for a in _secret("app").get("admins", [])]
            st.session_state["user"] = {"username": email, "name": str(u.get("name", "") or email),
                                        "role": "admin" if email.lower() in admins else "user"}
            return st.session_state["user"]
        render_header()
        with st.container(border=True):
            st.markdown("### Sign in")
            st.caption("Use your company Microsoft account.")
            st.button("Sign in with Microsoft", type="primary", width="stretch", on_click=st.login)
        st.stop()

    render_header()
    with st.container(border=True):
        st.markdown("### Sign in")
        if test_account_active():
            st.warning(f"**Test sign-in is active.** Username `{TEST_USER}` · password `{TEST_PASS}` (admin rights for testing). "
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
            user = None
            if test_account_active():
                if un == TEST_USER and pw == TEST_PASS:
                    user = {"username": un, "name": TEST_NAME, "role": "admin"}
            else:
                rec = _users().get(un)
                if rec and verify(pw, rec.get("password_hash", "")):
                    user = {"username": un, "name": rec.get("name", un), "role": rec.get("role", "user")}
            if user:
                att.pop(un, None)
                st.session_state["user"] = user
                st.rerun()
            fails += 1
            if fails >= MAX_TRIES:
                att[un] = [0, time.time() + LOCK_SECONDS]
                st.error(f"Too many attempts. Sign-in is blocked for {LOCK_SECONDS} seconds.")
            else:
                att[un] = [fails, 0.0]
                st.error("Incorrect username or password.")
    st.stop()
