from sqlalchemy import create_engine
import configparser

# Leer los datos de configuración desde el archivo config.ini
config = configparser.ConfigParser()
config.read('config/config.ini')

# Obtener los valores de configuración para Redshift
host = config.get('postgresql', 'host')
port = config.get('postgresql', 'port')
username = config.get('postgresql', 'username')
password = config.get('postgresql', 'pwd')
dbname = config.get('postgresql', 'dbname')

# Crear la cadena de conexión con Redshift
db_string = f"postgresql://{username}:{password}@{host}:{port}/{dbname}"

# Crear el objeto engine para conectarse a Redshift
engine = create_engine(db_string)

# Crear la tabla
schema = "nathy__coderhouse"

with engine.connect() as conn:
    conn.execute(
        f"""
            CREATE TABLE IF NOT EXISTS {schema}.current_weather (
                location TEXT NOT NULL,
                last_updated TIMESTAMP NOT NULL,
                temp_c DECIMAL(10, 2) NOT NULL,
                is_day INT NOT NULL,
                wind_kph DECIMAL(10, 2) NOT NULL,
                wind_degree INT NOT NULL,
                pressure_mb DECIMAL(10, 2) NOT NULL,
                pressure_in DECIMAL(10, 2) NOT NULL,
                precip_mm DECIMAL(10, 2) NOT NULL,
                humidity INT NOT NULL,
                cloud INT NOT NULL,
                vis_km DECIMAL(10, 2) NOT NULL,
                uv DECIMAL(10, 2) NOT NULL,
                gust_kph DECIMAL(10, 2) NOT NULL,
                "condition.code" INT NOT NULL
            ) 
            DISTKEY(location)    
            sortkey(last_updated);
        """
    )

    conn.execute(
        f"""
            CREATE TABLE IF NOT EXISTS {schema}.forecast_weather (
                date DATE NOT NULL,
                "day.maxtemp_c" DECIMAL(10, 2) NOT NULL,
                "day.mintemp_c" DECIMAL(10, 2) NULL,
                "day.avgtemp_c" DECIMAL(10, 2) NULL,
                "day.maxwind_kph" DECIMAL(10, 2) NULL,
                "day.totalprecip_in" DECIMAL(10, 2) NULL,
                "day.totalsnow_cm" DECIMAL(10, 2) NULL,
                "day.avgvis_km" DECIMAL(10, 2) NULL,
                "day.avghumidity" DECIMAL(10, 2) NULL,
                "day.daily_will_it_rain" DECIMAL(10, 2) NULL,
                "day.daily_will_it_snow" DECIMAL(10, 2) NULL,
                "day.daily_chance_of_rain" DECIMAL(10, 2) NULL,
                "day.daily_chance_of_snow" DECIMAL(10, 2) NULL,
                "day.uv" DECIMAL(10, 2) NULL,
                "day.condition.code" INT NOT NULL,
                "astro.sunrise" TEXT NOT NULL,
                "astro.sunset" TEXT NOT NULL,
                "astro.moonrise" TEXT NOT NULL,
                "astro.moonset" TEXT NOT NULL,
                "astro.moon_phase" TEXT NOT NULL,
                "astro.moon_illumination" DECIMAL(10, 2) NOT NULL,
                location TEXT NOT NULL
            )
            DISTKEY(location)    
            sortkey(date);
        """
    )
