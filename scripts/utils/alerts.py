import boto3

def send_sns_alert(context):
    """
    Função para enviar alerta via SNS.
    """
    sns_client = boto3.client("sns", region_name="us-east-1")
    topic_arn = "arn:aws:sns:us-east-1:123456789012:airflow-alerts"  # Substitua pelo ARN do seu tópico SNS

    # Construir mensagem
    message = f"""
    Task Failed:
    DAG: {context['task_instance'].dag_id}
    Task: {context['task_instance'].task_id}
    Execution Time: {context['execution_date']}
    Log URL: {context['task_instance'].log_url}
    """
    sns_client.publish(TopicArn=topic_arn, Message=message, Subject="Airflow Task Failure Alert")
