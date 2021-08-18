import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()


apiKey = os.getenv("API_KEY")

base_url = 'http://api.openweathermap.org/data/2.5/weather?'

def convertKelvintoFahrenheit(kelvin_temp):
    tempCelsius = kelvin_temp - 273.15
    ftemp = 9/5 * tempCelsius + 32
    return ftemp

def getCityTemperature(city):
    complete_url = base_url + "q=" + city + "&appid=" + apiKey
    response = requests.get(complete_url).json()
    if response["cod"] != '404':
        main = response["main"] 
        return convertKelvintoFahrenheit(main["temp"])