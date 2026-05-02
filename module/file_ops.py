import shutil
from shutil import unpack_archive, ReadError
import os
from os.path import basename
import json
from logging import error, info



# Copying a file
def copy_file(src, dst):
    shutil.copy(src, dst)

# Moving a file
def move_file(src, dst):
    shutil.move(src, dst)

# Making directory
def making_dir(name):
    os.makedirs(exist_ok=True, name=name)

# Extract file
def extract_file(file_path, output_folder):
    try:
        file_name = basename(file_path)

        unpack_archive(filename=file_path, extract_dir=output_folder)
        info(f"Extracting {file_name} to {output_folder}")
    except ReadError as err:
        error(f"Extract failed: {err}")

# Read file json
def read_json(file_name: str) -> dict:
    with open(file_name) as file:
        content = file.read()
        content_dict = json.load(content)
        return content_dict
    
# Write file json
def write_json(file_name: str, content: dict):
    with open(file_name, "w") as file:
        file.write(content)    