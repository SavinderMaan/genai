import requests

url = "http://127.0.0.1:8000/add"

payload = {
    "a": 10,
    "b": 20
}

response = requests.post(url, json=payload)

print("Status:", response.status_code)
print("Response:", response.json())
