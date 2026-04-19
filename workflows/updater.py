from core.download import download_file
from core.extractor import extract_file
from api.minecraft_api import _getVersion

version_link = _getVersion(attempt_val=5)
result = version_link["result"]["links"]

print("Versi yang tersedia")
print(version_link)
for num, server in enumerate(result):
    version = server["downloadUrl"]
    typeServer = server['downloadType']
    version = version.split("/")[-1]

    full_verion = typeServer + '_' + version
    print(f"{num}. {full_verion}.")

length_result = [a for a in range(len(result))]

while True:
    try:
        MC_version = int(input("pilih version yang kamu inginkan: "))
        if MC_version in length_result:
            link_server = result[MC_version]["downloadUrl"]
            download_file(url=link_server, timeout=30, retries=3)
            break
        print(f"Pilih angka diantara {len(result)}")
    except Exception:
        print("Angka tidak valid")
    



