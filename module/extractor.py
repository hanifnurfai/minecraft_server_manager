
from shutil import unpack_archive, ReadError
from logging import error, info
from os.path import basename

def extract_file(file_path, output_folder):
    try:
        file_name = basename(file_path)

        unpack_archive(filename=file_path, extract_dir=output_folder)
        info(f"Extracting {file_name} to {output_folder}")
    except ReadError as err:
        error(f"Extract failed: {err}")