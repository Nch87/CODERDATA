import psycopg2
from sqlalchemy import create_engine
import pandas as pd
import configparser
from pronostico import get_forecast_weather

def insert_forecast_data():
    config = configparser.ConfigParser()
    config.read('config/config.ini')

    # Establezco conexión con la base de datos
    conn = psycopg2.connect(
        host=config.get('postgresql', 'host'),
        port=config.get('postgresql', 'port'),
        user=config.get('postgresql', 'username'),
        password=config.get('postgresql', 'pwd'),
        dbname=config.get('postgresql', 'dbname')
    )

    # Creo string de conexión de SQLAlchemy
    db_string = "postgresql+psycopg2://" + config.get('postgresql', 'username') + ":" + config.get('postgresql', 'pwd') + "@" + config.get('postgresql', 'host') + ":" + config.get('postgresql', 'port') + "/" + config.get('postgresql', 'dbname')

    # Creo engine de SQLAlchemy
    engine = create_engine(db_string)

    # Obtengo el dataframe
    df = get_forecast_weather()

    # Eliminar la columna 'hour' del DataFrame
    df = df.drop('hour', axis=1)

    # Inserta los datos en la tabla
    df.to_sql('forecast_weather', engine, schema='nathy__coderhouse', if_exists='append', index=False)

    # Cierra conexión
    engine.dispose()
