from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
# Importando as funções necessárias dos scripts
from scripts.bronze.ingestion import ingest_data
from scripts.silver.transformation import transform_data
from scripts.gold.aggregation import aggregate_data
from scripts.gold.enrichment import enrich_data
from scripts.gold.formatting import format_data
from scripts.gold.finalization import finalize_data
from scripts.utils.alerts import send_sns_alert

# Definindo os argumentos padrão
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'start_date': datetime(2024, 11, 1),
    'email_on_failure': True,  # Enviar e-mail em caso de falha
    'email_on_retry': False,  # Não enviar e-mail em caso de tentativa de reexecução
    'email': ['seu_email@dominio.com'],  # E-mail para receber notificações
}

# Definindo a DAG com agendamento diário
dag = DAG(
    'aih_pipeline',
    default_args=default_args,
    description='Pipeline de Dados AIH',
    schedule_interval='@daily',  # Agendamento diário
)

# Tarefa 1
ingest_task = PythonOperator(
    task_id='ingest_data',
    python_callable=ingest_data,
    dag=dag
)

# Tarefa 2
transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=dag
)

# Tarefa 3: Agregação (Camada Gold)
aggregate_task = PythonOperator(
    task_id="aggregate_data",
    python_callable=aggregate_data,
    dag=dag
)

# Tarefa 4: Enriquecimento (Camada Gold)
enrich_task = PythonOperator(
    task_id="enrich_data",
    python_callable=enrich_data,
    dag=dag
)

# Tarefa 5: Formatação (Camada Gold)
format_task = PythonOperator(
    task_id="format_data",
    python_callable=format_data,
    dag=dag
)

# Tarefa 6: Finalização (Camada Gold)
finalize_task = PythonOperator(
    task_id="finalize_data",
    python_callable=finalize_data,
    dag=dag
)

ingest_task = PythonOperator(
    task_id="ingest_data",
    python_callable=ingest_data,
    on_failure_callback=send_sns_alert,
    dag=dag,
)

# Definindo a ordem das tarefas
# Definir a ordem das tarefas
ingest_task >> transform_task >> aggregate_task >> enrich_task >> format_task >> finalize_task

