import os
import boto3
from botocore.exceptions import NoCredentialsError
from datetime import datetime

# Configurações AWS
AWS_ACCESS_KEY = 'sua_chave_de_acesso'
AWS_SECRET_KEY = 'sua_chave_secreta'
BUCKET_NAME = 'ds-aih-bronze'

# Diretório local para arquivos temporários
LOCAL_TEMP_DIR = './temp/'

# Função para upload ao S3
def upload_to_s3(file_path, bucket_name, s3_key):
    try:
        # Cliente S3
        s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)
        
        # Upload
        s3.upload_file(file_path, bucket_name, s3_key)
        print(f"[{datetime.now()}] Sucesso: '{file_path}' enviado para '{bucket_name}/{s3_key}'")
    except FileNotFoundError:
        print(f"[{datetime.now()}] Erro: Arquivo '{file_path}' não encontrado.")
    except NoCredentialsError:
        print(f"[{datetime.now()}] Erro: Credenciais AWS inválidas.")

# Função de ingestão
def ingest_data_to_s3():
    # Verifica diretório temporário
    if not os.path.exists(LOCAL_TEMP_DIR):
        os.makedirs(LOCAL_TEMP_DIR)
    
    # Simula criação/ingestão de arquivos
    # Substitua isso pelo código de extração de dados real
    arquivos = ['dados1.csv', 'dados2.csv']
    for arquivo in arquivos:
        # Caminho local do arquivo
        file_path = os.path.join(LOCAL_TEMP_DIR, arquivo)
        
        # Simula criação de arquivo local
        with open(file_path, 'w') as f:
            f.write('id,nome,idade\n1,João,30\n2,Maria,25')
        print(f"[{datetime.now()}] Arquivo gerado: {file_path}")
        
        # Define a chave do arquivo no S3
        s3_key = f"bronze/{arquivo}"
        
        # Envia para o S3
        upload_to_s3(file_path, BUCKET_NAME, s3_key)
    
    # Limpa arquivos temporários
    for arquivo in arquivos:
        os.remove(os.path.join(LOCAL_TEMP_DIR, arquivo))
        print(f"[{datetime.now()}] Arquivo local removido: {arquivo}")

# Execução do script
if __name__ == "__main__":
    ingest_data_to_s3()
