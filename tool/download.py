import requests
from bs4 import BeautifulSoup


class serverUpdate:
  def __init__(self):
    self.MCbedrock = "https://www.minecraft.net/en-us/download/server/bedrock"
    self.MCjava = ""
  def _getContent(self):
    
    
  def check(self):
    

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "DNT": "1", # Do Not Track
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}

session_data = requests.Session()

try:
  response = session_data.get(MCBE_URL, headers=headers, timeout=20)
  print(f"Status Code: {response.status_code}")
    # Jika berhasil, print sebagian kontennya
  print(response.text[:200]) 
  with open("test.html", "w") as file:
    file.write(response.text)
except requests.exceptions.RequestException as e:
  print(f"Masih error: {e}")" 
