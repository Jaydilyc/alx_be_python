import requests

url = "https://api.weatherapi.com/v1/current.json"
params = {
    "key": "YOUR_API_KEY",
    "q": "Lagos"
}

response = requests.get(url, params=params)

print("Status Code:", response.status_code)
print("Raw Response:")
print(response.text)