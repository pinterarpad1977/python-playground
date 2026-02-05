from models import Vault, VaultEntry, VaultMetadata

pwd1 = VaultEntry("www.one.hu", "pururin", "mock_up_pwd")
pwd2 = VaultEntry("www.vodafone.hu", "ArpadPi", "mockup2", "old password")

v_meta = VaultMetadata()

vault = Vault(entries=[pwd1,pwd2], metadata=v_meta)

print(vault)

for entry in vault.entries:
    print(entry.service, entry.username, entry.password)
    