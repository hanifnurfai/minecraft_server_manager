from download import download_file
from extractor import extract_file
from minecraft_api import _getVersion
import os



def print_avaible_version(avaible_version):
    avaible_version_result = avaible_version["result"]["links"]
    
    for num, server in enumerate(avaible_version_result):
        version = server["downloadUrl"]
        typeServer = server['downloadType']
        version = version.split("/")[-1]

        full_verion = typeServer + '_' + version
        print(f"{num}. {full_verion}.")


def 