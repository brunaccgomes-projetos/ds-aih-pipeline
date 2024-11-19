from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Funções Python dos scripts existentes
from ingestion import ingest_data
from transformation import transform_data

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': True,
    'email': ['seu_email@gmail.com'],
    'retries': 1,
}

with DAG(
    'aih_data_pipeline',
    default_args=default_args,
    description='Pipeline de Ingestão e Transformação AIH',
    schedule_interval='@daily',
    catchup=False,
) as dag:

    task_ingest = PythonOperator(
        task_id='ingest_data',
        python_callable=ingest_data,
    )

    task_transform = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data,
    )

    task_ingest >> task_transform
