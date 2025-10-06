import os
import requests
from pathlib import Path
from urllib.parse import urlparse
from typing import List, Optional
import time


def create_dir_if_not_exist(output_dir) -> Path:
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    return output_path

def download_file(url: str, output_dir: Path, filename: Optional[str] = None) -> bool:
    try:
        # Extract filename from URL if not provided
        if filename is None:
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)

        file_path = output_dir / filename

        # Skip if file already exists
        if file_path.exists():
            print(f"File already exists: {filename}")
            return True

        print(f"Downloading: {filename}")

        # Download with progress
        response = requests.get(url, stream=True)
        response.raise_for_status()

        # Get file size for progress tracking
        total_size = int(response.headers.get('content-length', 0))

        with open(file_path, 'wb') as file:
            downloaded = 0
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
                    downloaded += len(chunk)
                    if total_size > 0:
                        progress = (downloaded / total_size) * 100
                        print(f"\rProgress: {progress:.1f}%", end='', flush=True)

        print(f"\nDownloaded: {filename} ({downloaded} bytes)")
        return True

    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error downloading {url}: {e}")
        return False


def download_files(urls: List[str], output_dir: str = "out", max_files: Optional[int] = None) -> None:
    # Create output directory
    output_path = create_dir_if_not_exist(output_dir)
    print(f"Output directory: {output_path.absolute()}")

    # Limit number of files if specified
    if max_files:
        urls = urls[:max_files]
        print(f"Downloading first {max_files} files...")

    successful_downloads = 0

    for i, url in enumerate(urls, 1):
        print(f"\n[{i}/{len(urls)}] Processing: {url}")

        # Download file
        if download_file(url, output_path):
            successful_downloads += 1

        # Add small delay to be respectful to the server
        time.sleep(0.1)

    print(f"\nDownload Summary:")
    print(f"Total files processed: {len(urls)}")
    print(f"Successful downloads: {successful_downloads}")