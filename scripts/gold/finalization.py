from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def finalize_data():
    """
    Realiza a validação e encerramento do processo de dados na camada Gold.
    Pode incluir auditoria, limpeza e geração de arquivos finais.
    """
    # Inicia sessão Spark
    spark = SparkSession.builder.appName("Gold Finalization").getOrCreate()

    # Caminhos no S3
    formatted_path = "s3://ds-aih-gold/formatted_data/"
    final_gold_path = "s3://ds-aih-gold/final_data/"

    # Carregar dados formatados da camada Gold
    print("Carregando dados formatados da camada Gold...")
    formatted_df = spark.read.parquet(formatted_path)

    # Validação dos dados (exemplo de checagem simples)
    print("Iniciando validação dos dados...")
    if formatted_df.count() == 0:
        raise ValueError("Nenhum dado encontrado na camada Gold após formatação!")

    # Realizar ações finais: por exemplo, gerar sumários ou limpar dados
    print("Gerando sumário dos dados finalizados...")
    summary_df = formatted_df.describe()

    # Salvando dados validados e finalizados na camada Gold
    print("Salvando dados finalizados na camada Gold...")
    formatted_df.write.mode("overwrite").parquet(final_gold_path)

    # Salvando sumário em formato CSV (ou qualquer outro formato de saída)
    summary_df.write.mode("overwrite").csv("s3://ds-aih-gold/final_data/summary.csv")

    print("Dados finalizados e salvos com sucesso na camada Gold!")
