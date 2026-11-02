"""Create a Secrets block for one sign-in user.  Run:  python make_password_hash.py"""
import getpass
from ra.auth import hash_password

u = input("Username (e.g. jakukuata): ").strip().lower()
n = input("Full name (shown as 'Assessed by'): ").strip()
p = getpass.getpass("Password: ")
if p != getpass.getpass("Confirm password: "):
    raise SystemExit("Passwords do not match.")
print(f'\nPaste into Settings > Secrets:\n\n[users.{u}]\nname = "{n}"\npassword_hash = "{hash_password(p)}"\n')
