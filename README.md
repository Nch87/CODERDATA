# Proyecto Data Engineering 
Natalia Chazarreta Comisión 56005
# Pronóstico del Tiempo

Este proyecto se centra en obtener el pronóstico del tiempo de diferentes ubicaciones utilizando APIs de pronóstico del tiempo. El objetivo es obtener los datos meteorológicos de diferentes lugares y almacenarlos en una base de datos PostgreSQL para su posterior consulta y análisis.

## Configuración

Antes de ejecutar el proyecto, asegúrate de configurar correctamente las API keys y los parámetros de las API de pronóstico del tiempo en el archivo `config.ini`.

## Bibliotecas utilizadas

- Python 3.x
- Bibliotecas de Python: requests, pandas, yfinance, sqlalchemy

## Uso

1. Ejecuta el script `pronostico.py` o `clima.py` para obtener el pronóstico del tiempo de diferentes ubicaciones.
2. Los datos del pronóstico y el clima se almacenarán en una base de datos PostgreSQL.
3. Puedes realizar consultas y análisis de los datos almacenados utilizando consultas SQL en PostgreSQL.

## Estructura del Proyecto

- `pronostico.py`: Script para obtener el pronóstico del tiempo y almacenarlo en la base de datos.
- `clima.py`: Script para obtener el pronóstico del tiempo y almacenarlo en la base de datos.
- `configApi.ini`: Archivo de configuración que contiene las API keys y los parámetros de las API de pronóstico del tiempo.
- `config.ini`: Archivo de configuración que contiene la configuracio para la conexión con Redshift
- `README.md`: Documentación del proyecto.

# Creación de la tabla "current_weather"

En este proyecto, hemos creado una tabla llamada "current_weather" en una base de datos utilizando SQL. Esta tabla almacena los datos del clima actual para diferentes ubicaciones.

## Código

      -  CREATE TABLE IF NOT EXISTS {schema}.current_weather
           location TEXT NOT NULL,
           last_updated TIMESTAMP NOT NULL,
           temp_f DECIMAL(10, 2) NOT NULL,
           is_day INT NOT NULL,
           wind_kph DECIMAL(10, 2) NOT NULL,
           wind_degree INT NOT NULL,
           pressure_mb DECIMAL(10, 2) NULL,
           pressure_in DECIMAL(10, 2) NULL,
           precip_mm DECIMAL(10, 2) NULL,
           humidity INT NOT NULL,
           cloud INT NOT NULL,
           vis_km DECIMAL(10, 2) NULL,
           uv DECIMAL(10, 2) NULL,
           gust_kph DECIMAL(10, 2) NULL,
           condition_code INT NOT NULL
       DISTKEY(lugar)    
       sortkey(last_updated);

       
## Descripción de la tabla

La tabla "current_weather" tiene las siguientes columnas y tipos de datos:

- `location`: una cadena de texto que representa la ubicación del clima actual.
- `last_updated`: una marca de tiempo que indica cuándo se actualizó por última vez el registro.
- `temp_f`: un número de punto flotante que representa la temperatura en grados fahrenheit.
- `is_day`: un valor entero (0 o 1) que indica si es de día o de noche.
- `wind_kph`: un número de punto flotante que representa la velocidad del viento en kilómetros por hora.
- `wind_degree`: un valor entero que representa la dirección del viento en grados.
- `pressure_mb`: un número de punto flotante que representa la presión atmosférica en milibares.
- `pressure_in`: un número de punto flotante que representa la presión atmosférica en pulgadas.
- `precip_mm`: un número de punto flotante que representa la cantidad de precipitación en milímetros.
- `humidity`: un valor entero que representa el porcentaje de humedad.
- `cloud`: un valor entero que representa el porcentaje de nubosidad.
- `vis_km`: un número de punto flotante que representa la visibilidad en kilómetros.
- `uv`: un número de punto flotante que representa el índice UV.
- `gust_kph`: un número de punto flotante que representa la ráfaga máxima del viento en kilómetros por hora.
- `condition_code`: un valor entero que representa el código de condición del clima.

- `La tabla está diseñada con una clave de distribución (DISTKEY) en la columna "location" y una clave de ordenamiento (sortkey) en la columna "last_updated". Esto ayuda a mejorar el rendimiento y la eficiencia al realizar consultas en la tabla`.

- `Esta tabla proporciona una estructura organizada para almacenar y consultar los datos del clima actual`.

- # Creación de la tabla "forecast_weather"
  
En este proyecto, hemos creado una tabla llamada "forecast_weather" en una base de datos utilizando SQL. Esta tabla almacena los datos del pronosstico extendido por 3 dias para diferentes ubicaciones.

## Código

      -  CREATE TABLE IF NOT EXISTS {schema}.current_weather
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
       DISTKEY(lugar)    
       sortkey(last_updated);
## Descripción de la tabla

La tabla "forecast_weather" tiene las siguientes columnas y tipos de datos:

- `date`: una fecha que indica la fecha de los datos del clima.
- `day_maxtemp_f`: un número de punto flotante que representa la temperatura máxima del día en grados Celsius.
- `day_mintemp_f`: un número de punto flotante que representa la temperatura mínima del día en grados Celsius.
- `day_avgtemp_f`: un número de punto flotante que representa la temperatura promedio del día en grados Celsius.
- `day_maxwind_kph`: un número de punto flotante que representa la velocidad máxima del viento durante el día en kilómetros por hora.
- `day_totalprecip_in`: un número de punto flotante que representa la precipitación total durante el día en pulgadas.
- `day_totalsnow_cm`: un número de punto flotante que representa la acumulación total de nieve durante el día en centímetros.
- `day_avgvis_km`: un número de punto flotante que representa la visibilidad promedio durante el día en kilómetros.
- `day_avghumidity` : un número de punto flotante que representa la humedad promedio durante el día en porcentaje.
- `day.daily_will_it_rain` : 1 = Sí 0 = No  Lloverá o no
- `day.daily_will_it_snow ` : 1 = Sí 0 = No  ¿Nevará o no?
- `day.daily_chance_of_rain ` :  Probabilidad de lluvia como porcentaje
- `day.daily_chance_of_snow ` : Probabilidad de nieve como porcentaje
- `day_uv`: un número de punto flotante que representa el índice UV durante el día.
- `astro.sunrise`: una hora que indica el amanecer para la ubicación.
- `astro.sunset`: una hora que indica el atardecer para la ubicación.
- `astro.moonrise`: una hora que indica la salida de la luna para la ubicación.
- `astro.moonset`: una hora que indica la puesta de la luna para la ubicación.
- `astro.moon_phase`: un texto que indica la fase lunar.
- `astro.moon_illumination`: un entero que representa el porcentaje de iluminación lunar.
- `location`: un texto que indica la ubicación.

- `La tabla está diseñada con una clave de distribución (DISTKEY) en la columna "location" y una clave de ordenamiento (sortkey) en la columna "date". Esto ayuda a mejorar el rendimiento y la eficiencia al realizar consultas en la tabla`.

- `Esta tabla proporciona una estructura organizada para almacenar y consultar los datos del pronostico del clima`.

## Insertar Datos en las Tablas `current_weather` mediante el archivo `insertC.py` y en `forecast_weather` mediante el archivo `insertP.py`
- `Descripción`:
Estos archivo contiene un script en Python que inserta datos de clima y pronostico en sus respectivas tablas de PostgreSQL utilizando SQLAlchemy.

- `Configuración` :
Antes de ejecutar el script, es necesario configurar la conexión a la base de datos y las credenciales de la API del clima. Esto se realiza mediante el archivo `config.ini` ubicado en la carpeta `config`.

- `Conexión a la base de datos` :
El script utiliza la biblioteca psycopg2 para conectarse a la base de datos en RedFish. Se establece la conexión utilizando los parámetros de configuración definidos en el archivo `config.ini`.

- `Creación del engine de SQLAlchemy`:
Una vez que se establece la conexión, se crea un objeto engine de SQLAlchemy utilizando los mismos parámetros de configuración.

- `Obtención de datos`:
Los datos de clima se obtienen mediante una función externa llamada `get_current_weather_all()` y los del pronostico de la funcion llamada `get_forecast_weather()`, que devuelve un dataframe de Pandas con los datos del clima actual y pronostico extendido de 3 dias.

- `Inserción de datos en la tabla`:
Finalmente, se insertan los datos del dataframe en una tabla llamada `current_weather` y  `forecast_weather` en el esquema nathy__coderhouse utilizando el método to_sql() de Pandas. Si la tabla ya existe, los datos se agregan usando el parámetro `if_exists='append'`.

- `Cierre de la conexión`:
Después de insertar los datos, se cierra la conexión a la base de datos utilizando el método `dispose()` del objeto `engine`.

## DAG: dag_insert_clima

Este DAG utiliza Airflow para programar y ejecutar la inserción de datos climáticos actuales en una base de datos. El DAG contiene una tarea llamada `task_insert_data_current` que llama a la función `insert_current_data` desde el módulo `scripts.main`. El DAG está configurado para comenzar el 1 de agosto de 2022 a las 2:00 AM y se ejecuta cada 4 horas. Esto asegura que los datos climáticos actuales se actualicen regularmente en la base de datos.

## DAG: dag_insert_forecast_data

Este DAG también utiliza Airflow para programar y ejecutar la inserción de datos climáticos de pronóstico en una base de datos. El DAG contiene una tarea llamada `task_insert_data_forecast` que llama a la función `insert_forecast_data` desde el módulo `scripts.main`. El DAG está configurado para comenzar el 1 de agosto de 2022 a las 2:00 AM y se ejecuta cada 4 días. Esto garantiza que los datos climáticos de pronóstico se actualicen periódicamente en la base de datos.

## Utilización de Airflow y Docker

Airflow es una plataforma de programación y gestión de flujos de trabajo que permite programar y ejecutar tareas en un entorno distribuido. Para facilitar el despliegue y la administración de Airflow, es común utilizar Docker para crear contenedores aislados que contienen todas las dependencias y configuraciones necesarias.

En este caso, he utilizado Docker para crear un contenedor llamado `coderdata`, que contiene el entorno de Airflow junto con los `DAGs` y cualquier otra dependencia necesaria. Esto permite una fácil portabilidad y escalabilidad de tus flujos de trabajo, ya que el contenedor puede ser ejecutado en cualquier entorno compatible con Docker.

Dentro del contenedor `oderdata`, he configurado y ejecutado los dos DAGs mencionados anteriormente, `dag_insert_clima` y `dag_insert_forecast_data`, utilizando la biblioteca Airflow. Estos DAGs se encargan de la inserción regular de datos climáticos actuales y de pronóstico en una base de datos.

## DAG : dag_email

La función `enviar_email` se encarga de enviar un correo electrónico utilizando el protocolo `SMTP`. Utiliza la librería `smtplib` para establecer una conexión segura con el servidor `SMTP` de Gmail, y luego envía un correo electrónico con un asunto y cuerpo específicos. Además, maneja excepciones mediante un bloque `try-except`, capturando cualquier error que ocurra durante el envío del correo electrónico e imprimiendo un mensaje de error junto con la excepción. En caso de éxito, se imprime un mensaje indicando que el correo se envió correctamente.

La función `verificar_dag_clima` y `verificar_dag_forecast` verifica si los DAGs llamados `dag_insert_clima` y `dag_insert_forecast_data` se ejecutaron correctamente en los días correspondientes. Utiliza la sesión de `Airflow` para consultar las bases de datos y buscar los registros de ejecución de los DAGs dentro del rango de tiempo del día. Luego, imprime un mensaje indicando si el DAG se ejecutó correctamente o no.

El código también define los DAGs llamados `dag_smtp_email_automatico_clima` y `dag_smtp_email_automatico_forecast`, que se ejecutan cada 4 horas y cada 4 días respectivamente. Cada uno de ellos tiene dos tareas: `verificar_dag_clima` y `verificar_dag_forecast`, las cuales ejecutan las funciones antes mencionadas, y la tarea `enviar_email`, que ejecuta la función `enviar_email`. Además, se especifica que la función `enviar_email` se utilizará como callback en caso de fallo.

Estos DAGs están diseñados para monitorear la ejecución de los DAGs correspondientes y enviar un correo electrónico en caso de fallo.

## DAG : dag_Temp

Explicación del código:

1. Establece las importaciones necesarias, incluyendo módulos de `Airflow`, `psycopg2` para la conexión a la base de datos `PostgreSQL`, y `smtplib` para enviar correos electrónicos.

2. Define un diccionario con argumentos por defecto para el flujo de trabajo de `Airflow`, incluyendo el propietario, la fecha de inicio y la configuración de reintentos.

3. Crea una función llamada `enviar_alerta_temperatura` que se encarga de realizar la consulta a la base de datos, procesar los resultados y enviar correos electrónicos si se cumple cierta condición.

4. Define un flujo de trabajo de Airflow con un nombre (dag_id) y una programación para ejecutar la función `enviar_alerta_temperatura` cada 4 horas.

5. Crea una tarea utilizando `PythonOperator` que ejecuta la función `enviar_alerta_temperatura` como parte del flujo de trabajo.

Este flujo de trabajo utiliza la biblioteca `Airflow` para programar y ejecutar tareas, la biblioteca `psycopg2` para conectarse a una base de datos PostgreSQL, y la biblioteca `smtplib` para enviar correos electrónicos. El código se encarga de enviar alertas por correo electrónico si la temperatura actual en una ubicación específica supera los 30 grados Celsius.

## DAG : dag_AlertaLluvias

Explicación del código:

1. Se importan los módulos necesarios, incluyendo `datetime`, `timedelta`, `DAG` y `PythonOperator de Airflow`, `psycopg2` para la conexión a la base de datos PostgreSQL, `smtplib` para enviar correos electrónicos, y ConfigParser para leer la configuración desde un archivo INI.

2. Se define un diccionario con argumentos por defecto para el flujo de trabajo de Airflow, incluyendo el propietario, la fecha de inicio, y la configuración de reintentos.

3. Se crea una función llamada `enviar_alerta_tormentas` que se encarga de realizar una consulta a la base de datos, procesar los resultados y enviar correos electrónicos si se cumple cierta condición.

4. Se define un flujo de trabajo de Airflow con un nombre (dag_id), una programación para ejecutar la función `enviar_alerta_tormentas` a las 10:00 AM todos los días, y se establece `catchup` como falso para evitar la ejecución retroactiva de tareas.

5. Se crea una tarea utilizando `PythonOperator` que ejecuta la función `enviar_alerta_tormentas` como parte del flujo de trabajo.

Este flujo de trabajo utiliza la biblioteca Airflow para programar y ejecutar tareas, la biblioteca psycopg2 para conectarse a una base de datos PostgreSQL, y la biblioteca smtplib para enviar correos electrónicos. El código se encarga de enviar alertas por correo electrónico si hay altas probabilidades de tormentas en una ubicación específica.

## Conexion de Api
- https://www.weatherapi.com/
