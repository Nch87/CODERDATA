from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from scripts.main import insert_current_data

default_args = {
    'retries': 5,
    'retry_delay': timedelta(minutes=1)
}

with DAG(
    default_args=default_args,
    dag_id='dag_insert_clima',
    start_date=datetime(2022, 8, 1, 2),
    catchup=False,
    schedule_interval="0 */4 * * *"
) as dag:
    
    dummy_start_task = DummyOperator(
        task_id="start"
    )
    
    task_insert_data_current = PythonOperator(
       task_id="insert_current_data",
       python_callable=insert_current_data,
       op_kwargs={
         "day": "{{execution_date.date()}}"
        }
    )
    
    dummy_end_task = DummyOperator(
        task_id="end"
    )
    
    dummy_start_task >> task_insert_data_current >> dummy_end_task
