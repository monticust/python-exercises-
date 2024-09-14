import requests 
import json
import time 
import datetime

def get_temperature(postcode):
    url =f"https://api.weatherapi.com/v1/current.json?key=20ebf4ecf36c43ee874151556240508&q={postcode}&aqi=no"
    page = requests.get(url)
    weather_json_string=page.text 
    

    # some JSON:

    # parse x:
    weather_dictionary = json.loads(weather_json_string)

    # the result is a Python dictionary

    

    temperature= weather_dictionary["current"]["temp_c"]

    return temperature 

file=open ('temperature.py.txt','w')


def write_temperature(date_string, temperature):
    print(date_string, temperature)
    file.write(f"{date_string},{temperature}\n")
    
    file.flush()


postcode="sa432nu"
temperature = get_temperature(postcode)



delay=300

while True:
    date_string=datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    write_temperature(date_string, temperature)
    temperature = get_temperature(postcode)
    time.sleep(delay)


 
    
    
    
    
    
    
    
