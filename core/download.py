from pathlib import Path
import requests
import time
import logging

api_request_header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

def download_file(url, timeout=10, retries=3, download_dir="tempFile") -> str:
    """
    Downloads a file from the given URL with retries.
    Returns the file path if successful, else None.
    """
    path = Path.cwd() / download_dir
    path.mkdir(parents=True, exist_ok=True)

    for attempt in range(retries):
        try:
            with requests.get(url, headers=api_request_header, stream=True, timeout=timeout) as req:
                req.raise_for_status()
                name_file = "-".join(url.split("/")[-2:])
                full_path = path / name_file

                with open(full_path, 'wb') as file:
                    for chunk in req.iter_content(chunk_size=8192):
                        file.write(chunk)

                logging.info("Download completed: %s", full_path)
                return str(full_path)
        except requests.RequestException as err:
            wait_time = (attempt + 1) ** 2
            logging.warning(f"Request Error: {err}. Retrying in {wait_time:.2f} seconds...")
            time.sleep(wait_time)
    logging.error("Download failed after %d retries.", retries)
    return None