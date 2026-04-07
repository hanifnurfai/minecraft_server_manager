import os
import time
import requests
import re


_url='https://net-secondary.web.minecraft-services.net/api/v1.0/download/links'
_headers={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

_Path = os.path.join(os.getcwd(), "tempFile")

if not os.path.exists(_Path): 
    os.mkdir(_Path) 

def _getVersion(attempt_val=5) -> dict:
    """get version and download link minecraft server.

    Args:
        attempt_val (int, optional): value for attempting. Defaults to 5.

    Returns:
        dict: result of version and link download minecraft server.
    """
    for attempt in range(attempt_val):
        try:
            session = requests.get(
                _url,
                headers=_headers,
                timeout=10
            )

            return session.json()
        
        except requests.exceptions.RequestException as req_err:
            wait_time = (attempt + 1) ** 2
            print(f"Request Error: {req_err}. Retrying in {wait_time:.2f} seconds...")
            time.sleep(wait_time)
    raise Exception("Timeout, try again later")
        
def downloadVersion(url):
    with requests.get(url=url, stream=True) as req:
        req.raise_for_status()
        name_file = re.split("/", url)[-2:]
        full_path = os.path.join(_Path, "_".join(name_file))

        with open(full_path, 'wb') as file:
            for chunk in req.iter_content(chunk_size=8192):
                file.write(chunk)
        print("Done downloading")    
    
content = _getVersion(3)
print("Avaible version:")
for num, link in enumerate(content["result"]["links"]):
    versionType, downloadURL = link.values()
    minecraVersion = re.split("/", downloadURL)[-2:]
    print(f"{num + 1}. {versionType}: {"_".join(minecraVersion)}")

choosedVersion = int(input("Choose version that you want to download based order: ")) - 1
full_link = content["result"]['links'][choosedVersion]["downloadUrl"]
downloadVersion(full_link)
