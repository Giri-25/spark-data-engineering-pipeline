import os
import urllib.request
from urllib.error import HTTPError, URLError

# Working dataset URL
DATA_URL = "https://vega.github.io/vega-datasets/data/cars.json"

OUTPUT_DIR = "data/raw"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "cars.json")


def download_dataset():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("=" * 60)
    print("Downloading dataset...")
    print(f"URL: {DATA_URL}")
    print("=" * 60)

    try:
        urllib.request.urlretrieve(DATA_URL, OUTPUT_FILE)
        print("\n✅ Download Successful!")
        print(f"Saved to: {OUTPUT_FILE}")

    except HTTPError as e:
        print(f"\nHTTP Error: {e.code} - {e.reason}")

    except URLError as e:
        print(f"\nURL Error: {e.reason}")

    except Exception as e:
        print(f"\nUnexpected Error: {e}")


if __name__ == "__main__":
    download_dataset()