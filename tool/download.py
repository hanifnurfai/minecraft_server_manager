import requests
from bs4 import BeautifulSoup



MCBE_url = "https://www.minecraft.net/en-us/download/server/bedrock"
MCJAVA_url = "https://www.minecraft.net/en-us/download/server/"

content = requests.get(MCBE_url)
#data = BeautifulSoup(content, "lxml")
print(content.status_code)