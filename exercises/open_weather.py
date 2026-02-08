import requests

# 1) Geocode city name -> lat/lon (no key)
geo = requests.get(
    "https://geocoding-api.open-meteo.com/v1/search",
    params={"name": "Lagos", "count": 1},
    timeout=15
).json()

lat = geo["results"][0]["latitude"]
lon = geo["results"][0]["longitude"]

# 2) Get current weather (no key)
weather = requests.get(
    "https://api.open-meteo.com/v1/forecast",
    params={"latitude": lat, "longitude": lon, "current_weather": "true"},
    timeout=15
).json()

current = weather["current_weather"]
print("Temperature:", current["temperature"])
print("Wind Speed:", current["windspeed"])