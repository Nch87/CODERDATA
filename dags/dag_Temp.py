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

def enviar_alerta_temperatura(**context):
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
    cur.execute("SELECT location, temp_c, DATE(last_updated) as fecha_actualizada FROM current_weather WHERE DATE(last_updated) = CURRENT_DATE")
    result = cur.fetchall()

    for location, temp_c, last_updated in result:
        if temp_c > 30:
            try:
                x = smtplib.SMTP('smtp.gmail.com', 587)
                x.starttls()
                gmail_user = 'nchazarreta.comision56005@gmail.com'
                gmail_password = Variable.get('GMAIL_SECRET')
                x.login(gmail_user, gmail_password)

                subject = f'Alerta de temperatura alta en {location}'
                body_text = f'La temperatura actual en {location} es {temp_c} C. Última actualización: {last_updated.strftime("%Y-%m-%d")}'
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
    dag_id='dag_alerta_temperatura',
    schedule_interval="30 */4 * * *",
    default_args=default_args,
    catchup=False,
) as dag:
    tarea_enviar_alerta_temperatura = PythonOperator(
        task_id='enviar_alerta_temperatura',
        python_callable=enviar_alerta_temperatura,
        provide_context=True,
    )
