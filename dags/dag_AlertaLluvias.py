from datetime import datetime, timedelta
from airflow.models import DAG, Variable
from airflow.operators.python import PythonOperator
import psycopg2
import smtplib
from configparser import ConfigParser


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 11, 10),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def enviar_alerta_tormentas(**context):
    config = ConfigParser()
    config.read('config/config.ini')

    conn = psycopg2.connect(
        host=config.get('postgresql', 'host'),
        port=config.get('postgresql', 'port'),
        user=config.get('postgresql', 'username'),
        password=config.get('postgresql', 'pwd'),
        dbname=config.get('postgresql', 'dbname')
    )

    cur = conn.cursor()
    cur.execute("SELECT location, \"day.daily_chance_of_rain\" , date FROM forecast_weather WHERE date = CURRENT_DATE")
    result = cur.fetchall()

    for location, daily_chance_of_rain , date in result:
        if daily_chance_of_rain > 75:
            try:
                x = smtplib.SMTP('smtp.gmail.com', 587)
                x.starttls()
                gmail_user = 'nchazarreta.comision56005@gmail.com'
                gmail_password = Variable.get('GMAIL_SECRET')
                x.login(gmail_user, gmail_password)

                subject = f'Alerta de tormentas {location}'
                body_text = f'Altas probabilidades de tormentas en {location} con {daily_chance_of_rain} % de probabilidades. Última actualización: {date}'
                subject = subject.encode('utf-8')
                body_text = body_text.encode('utf-8')

                message = f'Subject: {subject}\n\n{body_text}'

                x.sendmail(gmail_user, 'nchazarreta.comision56005@gmail.com', message)
                print('Correo enviado con éxito')
            except Exception as e:
                print(f'Error al enviar correo: {e}')
    cur.close()
    conn.close()

with DAG( 
    dag_id='dag_alerta_tormentas',
    schedule_interval="0 10 * * *",
    default_args=default_args,
    catchup=False,
) as dag:
    tarea_enviar_alerta_tormentas = PythonOperator(
        task_id='enviar_alerta_tormentas',
        python_callable=enviar_alerta_tormentas,
        provide_context=True,
    )
