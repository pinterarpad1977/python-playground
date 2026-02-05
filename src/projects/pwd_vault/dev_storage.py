from storage import load_salt, load_vault, save_vault
from crypto import derive_key
from models import Vault, VaultEntry
from config import SALT_FILE, VAULT_FILE

#load or create salt
salt = load_salt(SALT_FILE)

#derive key from master password
key = derive_key("testpassword", salt)

# create a vault with one entry
vault = Vault(entries=[VaultEntry("gmail", "Arpad", "222", "new")])

# save it
save_vault(VAULT_FILE, vault, key)
#print("Vault saved")
# load it back
loaded = load_vault(VAULT_FILE, key)
print(loaded)
#print(loaded.entries[0].password)
#print(loaded.entries[0].service)
