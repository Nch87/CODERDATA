from datetime import datetime, timedelta
from airflow.models import DAG, Variable
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from airflow.models import DagRun
from airflow import settings

import smtplib

def enviar_email(**context):
    try:
        x = smtplib.SMTP('smtp.gmail.com',587)
        x.starttls()
        
        print(f"Mi clave es: {Variable.get('GMAIL_SECRET')}")
        x.login(
            'nchazarreta.comision56005@gmail.com',
            Variable.get('GMAIL_SECRET')
        )

        subject = f'Airflow reporte {context["dag"]} {context["execution_date"]}'
        body_text = f'Tarea {context["task_instance_key_str"]} ejecutada'
        message='Subject: {}\n\n{}'.format(subject,body_text)
        
        x.sendmail('nchazarreta.comision56005@gmail.com', 'nchazarreta.comision56005@gmail.com', message)
        print('Exito')
    except Exception as exception:
        print(exception)
        print('Failure')

def verificar_dag_clima(**context):
    # Obtengo la fecha de inicio y fin del día actual
    start_of_day = context['execution_date'].replace(hour=0, minute=0, second=0, microsecond=0)
    end_of_day = start_of_day + timedelta(days=1)

    # Obtengo el ID del DAG que se desea verificar
    dag_id = 'dag_insert_clima'

    # Busca el registro de ejecución del DAG dentro del rango de tiempo del día actual
    session = settings.Session()
    dagrun = session.query(DagRun).filter(
        DagRun.dag_id == dag_id,
        DagRun.execution_date >= start_of_day,
        DagRun.execution_date < end_of_day
    ).order_by(DagRun.execution_date.desc()).first()

    if dagrun:
        if dagrun.state == 'success':
            print(f'El DAG {dag_id} se ejecutó correctamente el {dagrun.execution_date}')
        else:
            print(f'El DAG {dag_id} no se ejecutó correctamente el {dagrun.execution_date}')
    else:
        print(f'No se encontró registro de ejecución para el DAG {dag_id} en el día actual')

    session.close() 

with DAG( 
    dag_id='dag_smtp_email_automatico_clima',
    schedule_interval="30 */4 * * *",
    on_failure_callback=enviar_email,
    catchup=False,
    start_date=datetime(2023,11,10)
) as dag:
    tarea_verificar_dag_clima = PythonOperator(
        task_id='verificar_dag_clima',
        python_callable=verificar_dag_clima,
        provide_context=True,
    )

    tarea_enviar_email = PythonOperator(
        task_id='enviar_email',
        python_callable=enviar_email,
        provide_context=True,
    )

    tarea_verificar_dag_clima >> tarea_enviar_email
      