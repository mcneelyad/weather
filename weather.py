
import json
import requests
import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')

base_url = 'http://api.openweathermap.org/data/2.5/weather?'

city_names = ['Charlotte','New York City','Los Angeles','Chicago','Houston','Phoenix']

temperatures = []
pressures = []
humidities = []
descriptions = []

def temp_to_fahrenheit(kelvin_temp):
    ftemp = ((kelvin_temp-273.15)*9)/5
    return ftemp


for city in city_names:

    complete_url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url).json()
    #print(response)
    if response["cod"] != '404':
        main = response["main"] 
        temperatures.append(temp_to_fahrenheit(main["temp"]))
        pressures.append(main["pressure"])
        humidities.append(main["humidity"])
        weather = response["weather"] 
        descriptions.append(weather[0]["description"])
    else:
        print('City not found')

columns = ['City Name','Temperature','Pressure','Humdity','Description']

df = pd.DataFrame(list(zip(city_names,temperatures,pressures,humidities,descriptions)),columns=columns)

# df.to_csv('weather_data.csv',index=False)