from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Configuração do Spark
spark = SparkSession.builder \
    .appName("Transformacao_AIH") \
    .getOrCreate()

# Caminhos no Amazon S3 (ajuste conforme sua estrutura de buckets)
BUCKET_NAME = "seu-bucket-s3"
BRONZE_PATH = f"s3a://{BUCKET_NAME}/bronze/"
SILVER_PATH = f"s3a://{BUCKET_NAME}/silver/"

def transformar_dados():
    """
    Função para limpar e padronizar os dados da camada Bronze e salvá-los na camada Silver.
    """
    try:
        # Leitura dos dados da camada Bronze
        print("Iniciando leitura dos dados da camada Bronze...")
        dados_bronze = spark.read.csv(
            f"{BRONZE_PATH}aih_dados.csv", header=True, inferSchema=True
        )
        
        print("Dados carregados com sucesso. Iniciando transformação...")

        # Transformações principais
        dados_silver = (
            dados_bronze
            .filter(col("custo_total").isNotNull())  # Filtrar registros com custo válido
            .select(
                col("cid_principal").alias("diagnostico_principal"),
                col("tempo_internacao").cast("int"),
                col("custo_total").cast("double"),
                col("tipo_hospital"),
                col("data_admissao"),
                col("data_alta")
            )
        )

        # Salvando os dados transformados na camada Silver
        print("Salvando dados transformados na camada Silver...")
        dados_silver.write.mode("overwrite").parquet(SILVER_PATH)

        print("Transformação concluída com sucesso e dados salvos na camada Silver.")

    except Exception as e:
        print(f"Erro durante a transformação dos dados: {e}")

# Execução da função de transformação
if __name__ == "__main__":
    transformar_dados()
