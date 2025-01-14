import requests
from tqdm import tqdm
from os import path

def download_url(url: str, filepath: str) -> None:
    """
    Stream the given URL to the given file path.
    """

    if path.exists(filepath):
        # TODO: check ETag and Last-Modified headers to see if we need to download the file again
        print(f"File {filepath} already exists, skipping download")
        return

    # Streaming, so we can iterate over the response.
    response = requests.get(url, stream=True)
    response.raise_for_status()

    # Sizes in bytes.
    total_size = int(response.headers.get("content-length", 0))
    block_size = 1024 * 1024 * 4  # 4 MB

    with tqdm(total=total_size, unit="B", unit_scale=True) as progress_bar:
        with open(filepath, "wb") as file:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                file.write(data)

    if total_size != 0 and progress_bar.n != total_size:
        raise RuntimeError(f"Could not download file, got {progress_bar.n} bytes out of {total_size} bytes")
    else:
        print(f"Downloaded {progress_bar.n} bytes to {filepath} successfully")
