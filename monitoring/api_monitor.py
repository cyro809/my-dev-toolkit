import requests
import time

URL = "https://api.example.com/status"

while True:
    response = requests.get(URL)

    if response.status_code != 200:
        print("API is down!")
    else:
        print("API OK")

    time.sleep(60)