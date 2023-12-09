from configparser import ConfigParser
import requests
import json
import pandas as pd

config = ConfigParser()
config.read('config/configApi.ini')

def get_forecast_weather():
    results = []

    # Función 1
    url_base = config.get('api_Pronostico', 'url_base')
    endpoint = config.get('api_Pronostico', 'endpoint')
    key = config.get('api_Pronostico', 'key')
    q = config.get('api_Pronostico', 'q')
    days = config.get('api_Pronostico', 'days')
    aqi = config.get('api_Pronostico', 'aqi')
    alerts = config.get('api_Pronostico', 'alerts')
    location = 'Buenos Aires_ARG'  

    url = f"{url_base}/{endpoint}?key={key}&q={q}&days={days}&aqi={aqi}&alerts={alerts}"
    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)
        result = pd.json_normalize(data["forecast"]["forecastday"])
        result['location'] = location  
        results.append(result)

    # Función 2
    url_base = config.get('api_Pronostico2', 'url_base')
    endpoint = config.get('api_Pronostico2', 'endpoint')
    key = config.get('api_Pronostico2', 'key')
    q = config.get('api_Pronostico2', 'q')
    days = config.get('api_Pronostico2', 'days')
    aqi = config.get('api_Pronostico2', 'aqi')
    alerts = config.get('api_Pronostico2', 'alerts')
    location = 'La Paz_BOL'  

    url = f"{url_base}/{endpoint}?key={key}&q={q}&days={days}&aqi={aqi}&alerts={alerts}"
    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)
        result = pd.json_normalize(data["forecast"]["forecastday"])
        result['location'] = location 
        results.append(result)

    # Función 3
    url_base = config.get('api_Pronostico3', 'url_base')
    endpoint = config.get('api_Pronostico3', 'endpoint')
    key = config.get('api_Pronostico3', 'key')
    q = config.get('api_Pronostico3', 'q')
    days = config.get('api_Pronostico3', 'days')
    aqi = config.get('api_Pronostico3', 'aqi')
    alerts = config.get('api_Pronostico3', 'alerts')
    location = 'Asuncion_PRY'  

    url = f"{url_base}/{endpoint}?key={key}&q={q}&days={days}&aqi={aqi}&alerts={alerts}"
    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)
        result = pd.json_normalize(data["forecast"]["forecastday"])
        result['location'] = location  
        results.append(result)

    # Función 4
    url_base = config.get('api_Pronostico4', 'url_base')
    endpoint = config.get('api_Pronostico4', 'endpoint')
    key = config.get('api_Pronostico4', 'key')
    q = config.get('api_Pronostico4', 'q')
    days = config.get('api_Pronostico4', 'days')
    aqi = config.get('api_Pronostico4', 'aqi')
    alerts = config.get('api_Pronostico4', 'alerts')
    location = 'Santiago_CHL'  

    url = f"{url_base}/{endpoint}?key={key}&q={q}&days={days}&aqi={aqi}&alerts={alerts}"
    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)
        result = pd.json_normalize(data["forecast"]["forecastday"])
        result['location'] = location  
        results.append(result)

  
    final_result = pd.concat(results, ignore_index=True)
    final_result['location'] = final_result['location'].str.replace('_', ' ')  

    return final_result

results = get_forecast_weather()
print(results)
