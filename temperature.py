import requests 
import json

url = "https://api.weatherapi.com/v1/current.json?key=20ebf4ecf36c43ee874151556240508&q=SA432NU&aqi=no"
page = requests.get(url)
weather_json_string=page.text 
print(weather_json_string)

# some JSON:

# parse x:
weather_dictionary = json.loads(weather_json_string)

# the result is a Python dictionary

print(weather_dictionary["current"]["temp_c"])