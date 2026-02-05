from storage import load_salt

salt1 = load_salt("vault.salt")
salt2 = load_salt("vault.salt")

print(salt1 == salt2)

