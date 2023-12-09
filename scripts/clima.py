from configparser import ConfigParser
import requests
import json
import pandas as pd

config = ConfigParser()
config.read('config/configApi.ini')

# Conexion a Base Clima Actual

def get_current_weather_all():
    results = []

    # Función 1
    url_base = config.get('api_ClimaActual', 'url_base')
    endpoint = config.get('api_ClimaActual', 'endpoint')
    key = config.get('api_ClimaActual', 'key')
    q = config.get('api_ClimaActual', 'q')
    aqi = config.get('api_ClimaActual', 'aqi')
    location = 'Buenos Aires_ARG'  
    url = f"{url_base}/{endpoint}?key={key}&q={q}&aqi={aqi}"
    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)
        result = pd.json_normalize(data["current"])
        result['location'] = location  
        results.append(result)


    # Función 2
    url_base = config.get('api_ClimaActual2', 'url_base')
    endpoint = config.get('api_ClimaActual2', 'endpoint')
    key = config.get('api_ClimaActual2', 'key')
    q = config.get('api_ClimaActual2', 'q')
    aqi = config.get('api_ClimaActual2', 'aqi')
    location = 'La Paz_BOL' 

    url = f"{url_base}/{endpoint}?key={key}&q={q}&aqi={aqi}"
    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)
        result = pd.json_normalize(data["current"])
        result['location'] = location  
        results.append(result)


    # Función 3
    url_base = config.get('api_ClimaActual3', 'url_base')
    endpoint = config.get('api_ClimaActual3', 'endpoint')
    key = config.get('api_ClimaActual3', 'key')
    q = config.get('api_ClimaActual3', 'q')
    aqi = config.get('api_ClimaActual3', 'aqi')
    location = 'Asuncion_PRY' 

    url = f"{url_base}/{endpoint}?key={key}&q={q}&aqi={aqi}"
    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)
        result = pd.json_normalize(data["current"])
        result['location'] = location 
        results.append(result)


    # Función 4
    url_base = config.get('api_ClimaActual4', 'url_base')
    endpoint = config.get('api_ClimaActual4', 'endpoint')
    key = config.get('api_ClimaActual4', 'key')
    q = config.get('api_ClimaActual4', 'q')
    aqi = config.get('api_ClimaActual4', 'aqi')
    location = 'Santiago_CHL'  

    url = f"{url_base}/{endpoint}?key={key}&q={q}&aqi={aqi}"
    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)
        result = pd.json_normalize(data["current"])
        result['location'] = location  
        results.append(result)

 
    final_result = pd.concat(results)
    final_result['location'] = final_result['location'].str.replace('_', ' ')

    return final_result

results = get_current_weather_all()
print(results)