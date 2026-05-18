from minecraft_api import avaible_version
from download import download_file
from file_ops import extract_file
import os

serverDir = "content/savedZIPServers"
server_list = os.listdir(serverDir) if os.path.isdir(serverDir) else None

def list_avaible_server():
    return server_list

def donwload_server(selected_version):
    downloadUrl = selected_version['downloadUrl']
    download_file(downloadUrl)

def update_server(selected_server):
    pass

        