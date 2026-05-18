import logging
import time
import requests


URL='https://net-secondary.web.minecraft-services.net/api/v1.0/download/links'
HEADER ={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

def avaible_version(attempt_val=5) -> dict:
    """get avaible version and download link minecraft server.

    Args:
        attempt_val (int, optional): value for attempting. Defaults to 5.

    Returns:
        dict: result of version and link download minecraft server.
    """
    for attempt in range(attempt_val):
        try:
            session = requests.get(
                URL,
                headers=HEADER,
                timeout=10
            )
            logging.info("Request completed", )
            return session.json()
        
        except requests.exceptions.RequestException as req_err:
            wait_time = (attempt + 1) ** 2
            logging.warning(f"Request Error: {req_err}. Retrying in {wait_time:.2f} seconds...")
            time.sleep(wait_time)
    logging.error("Download failed after %d retries.", attempt_val)
    return None

def main():
    print(avaible_version())

if __name__ == "__main__":
    main()