from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def format_data():
    """
    Formata os dados da camada Gold, realizando ajustes finais e salvando o formato desejado.
    """
    # Inicia sessão Spark
    spark = SparkSession.builder.appName("Gold Formatting").getOrCreate()

    # Caminhos no S3
    enriched_path = "s3://ds-aih-gold/enriched_data/"
    final_gold_path = "s3://ds-aih-gold/formatted_data/"

    # Carregar dados enriquecidos da camada Gold
    print("Carregando dados enriquecidos da camada Gold...")
    enriched_df = spark.read.parquet(enriched_path)

    # Formatação de dados
    print("Iniciando formatação dos dados...")
    formatted_df = enriched_df.select(
        "diagnostico", 
        "frequencia", 
        "custo_total", 
        "categoria"
    )

    # Salvando dados formatados na camada Gold
    print("Salvando dados formatados na camada Gold...")
    formatted_df.write.mode("overwrite").parquet(final_gold_path)

    print("Dados formatados e salvos com sucesso na camada Gold!")
