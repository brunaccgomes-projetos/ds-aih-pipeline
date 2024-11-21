import os
import boto3
import zipfile
import pandas as pd
import requests
from io import BytesIO

# Configurações AWS
AWS_ACCESS_KEY = 'sua_chave_de_acesso'
AWS_SECRET_KEY = 'sua_chave_secreta'
BUCKET_NAME = 'ds-aih-bronze'
LOCAL_TEMP_DIR = './temp/'

# Função de ingestão de dados
def ingest_data():
    # Exemplo de download de arquivos do DATASUS
    url = 'http://sistemas.datasus.gov.br/download'
    response = requests.get(url)
    
    # Baixar arquivo ZIP para o diretório temporário
    zip_file_path = os.path.join(LOCAL_TEMP_DIR, 'SIHSUS_SP_2018_2023.zip')
    with open(zip_file_path, 'wb') as f:
        f.write(response.content)

    # Extrair arquivo ZIP
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(LOCAL_TEMP_DIR)
    
    # Lógica para ler e carregar os arquivos CSV no S3
    for csv_file in os.listdir(LOCAL_TEMP_DIR):
        if csv_file.endswith('.csv'):
            file_path = os.path.join(LOCAL_TEMP_DIR, csv_file)
            data = pd.read_csv(file_path)
            s3_client = boto3.client(
                's3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY
            )
            s3_client.upload_file(file_path, BUCKET_NAME, f'bronze/{csv_file}')
            print(f'{csv_file} carregado para o S3.')

