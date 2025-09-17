# worker.py
import time
import requests

URL = "https://example.com"  # replace with your endpoint

while True:
    try:
        response = requests.get(URL, timeout=10)
        print(f"Status: {response.status_code} at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    except Exception as e:
        print(f"Error: {e}")

    # wait 12 minutes
    time.sleep(12 * 60)
