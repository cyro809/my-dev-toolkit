import requests

url = "https://api.example.com/users"

payload = {
    "name": "John",
    "email": "john@example.com"
}

response = requests.post(url, json=payload)

print(response.status_code)
print(response.json())