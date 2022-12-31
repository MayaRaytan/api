import requests

def kelvin_to_celsius(kelvin_degree):
    return kelvin_degree - 273.15

def get_current_temperature_in_celsius():
    URL = "http://api.openweathermap.org/data/2.5/weather"
    querry = input()
    key = "replace with your api key"
    call = URL + "?q=" + querry + "&appid=" + key
    api_response = requests.get(call).json()['main']['temp']
    return kelvin_to_celsius(api_response)

print(get_current_temperature_in_celsius())
