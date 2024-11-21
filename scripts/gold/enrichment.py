from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

def enrich_data():
    """
    Enriquecer dados da camada Silver, adicionando novas colunas e informações na camada Gold.
    """
    # Inicia sessão Spark
    spark = SparkSession.builder.appName("Gold Enrichment").getOrCreate()

    # Caminhos no S3
    silver_path = "s3://ds-aih-silver/dados_silver.parquet"
    gold_path = "s3://ds-aih-gold/enriched_data/"

    # Carregar dados da camada Silver
    print("Carregando dados da camada Silver...")
    silver_df = spark.read.parquet(silver_path)

    # Enriquecimento de dados
    print("Iniciando enriquecimento de dados...")
    enriched_df = silver_df.withColumn(
        "categoria",
        when(col("custo_total") > 1000, "Alto")
        .otherwise("Baixo")
    )

    # Salvando dados enriquecidos na camada Gold
    print("Salvando dados enriquecidos na camada Gold...")
    enriched_df.write.mode("overwrite").parquet(gold_path)

    print("Dados enriquecidos salvos com sucesso na camada Gold!")
