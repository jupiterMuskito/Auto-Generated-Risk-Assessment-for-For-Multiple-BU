"""Create Secrets entries.
  python make_password_hash.py           -> a sign-in user block ([users.<name>])
  python make_password_hash.py --admin   -> the Admin page password ([admin] password_hash)
"""
import getpass
import sys

from ra.auth import hash_password

if "--admin" in sys.argv:
    p = getpass.getpass("New admin password: ")
    if p != getpass.getpass("Confirm: "):
        raise SystemExit("Passwords do not match.")
    print(f'\nPaste into Settings > Secrets:\n\n[admin]\npassword_hash = "{hash_password(p)}"\n')
    raise SystemExit
u = input("Username (e.g. jakukuata): ").strip().lower()
n = input("Full name (shown as 'Assessed by'): ").strip()
p = getpass.getpass("Password: ")
if p != getpass.getpass("Confirm password: "):
    raise SystemExit("Passwords do not match.")
print(f'\nPaste into Settings > Secrets:\n\n[users.{u}]\nname = "{n}"\npassword_hash = "{hash_password(p)}"\n')
