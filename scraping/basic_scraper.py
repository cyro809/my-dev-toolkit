import requests
from bs4 import BeautifulSoup

URL = "https://example.com"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

items = []

for element in soup.select(".item"):
    title = element.get_text(strip=True)

    items.append({
        "title": title
    })

print(items)