from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, sum

def aggregate_data():
    """
    Agrega dados da camada Silver e gera tabelas analíticas na camada Gold.
    """
    # Inicia sessão Spark
    spark = SparkSession.builder.appName("Gold Aggregation").getOrCreate()

    # Caminhos no S3
    silver_path = "s3://ds-aih-silver/dados_silver.parquet"
    gold_path = "s3://ds-aih-gold/aggregated_data/"

    # Carregar dados da camada Silver
    print("Carregando dados da camada Silver...")
    silver_df = spark.read.parquet(silver_path)

    # Agregações
    print("Iniciando agregações...")
    aggregated_df = silver_df.groupBy("diagnostico").agg(
        count("*").alias("frequencia"),
        sum("custo_total").alias("custo_total")
    )

    # Salvando resultados na camada Gold
    print("Salvando dados agregados na camada Gold...")
    aggregated_df.write.mode("overwrite").parquet(gold_path)

    print("Dados agregados salvos com sucesso na camada Gold!")
