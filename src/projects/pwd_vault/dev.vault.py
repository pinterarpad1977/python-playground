from models import Vault
from vault import VaultManager

v = Vault()
mgr = VaultManager(v)

mgr.add_entry("gmail", "arpad", "secret")
mgr.add_entry("github", "arpad", "12345")

print(mgr.list_entries())
print(mgr.find_entries("git"))
mgr.remove_entry("gmail")
print(mgr.list_entries())
