from pprint import pprint
import requests

def get_waether() :
    API_KEY = ""

    lat = 37.56
    lon = 126.97

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"

    response = requests.get(url).json()
    return response