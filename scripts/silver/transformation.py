import os
import boto3
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Configurações AWS
AWS_ACCESS_KEY = 'sua_chave_de_acesso'
AWS_SECRET_KEY = 'sua_chave_secreta'
BUCKET_NAME = 'ds-aih-bronze'
S3_SILVER_BUCKET = 'ds-aih-silver'

# Iniciar a sessão do Spark
spark = SparkSession.builder \
    .appName('AIH Data Transformation') \
    .getOrCreate()

# Função para transformação de dados
def transform_data():
    s3_client = boto3.client(
        's3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY
    )
    
    # Baixar dados da camada bronze do S3
    s3_client.download_file(BUCKET_NAME, 'bronze/sihtables.csv', '/tmp/sihtables.csv')
    
    # Ler os dados com pandas (ou usar o spark diretamente)
    data = pd.read_csv('/tmp/sihtables.csv')

    # Aqui você pode aplicar transformações de limpeza e padronização
    # Exemplo: Filtrando as colunas necessárias
    cleaned_data = data[['id', 'diagnostic', 'cost']]
    
    # Salvar os dados transformados no S3 (na camada Silver)
    silver_df = spark.createDataFrame(cleaned_data)
    silver_df.write.mode('overwrite').parquet(f's3://{S3_SILVER_BUCKET}/silver_data/')
    print("Dados transformados para a camada Silver e armazenados no S3.")
