from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Configuração da sessão Spark
spark = SparkSession.builder.appName("TransformacaoAIH").getOrCreate()

# Caminho das camadas
bronze_path = "adl://seu_data_lake/bronze-dados"
silver_path = "adl://seu_data_lake/silver-dados"

def transformar_dados():
    """
    Realiza a transformação inicial dos dados da camada Bronze para Silver.
    """
    # Leitura dos dados brutos
    df = spark.read.csv(f"{bronze_path}/*.csv", header=True, inferSchema=True)
    
    # Filtrar e limpar colunas principais
    colunas_principais = ["Ano", "CID_Principal", "Tempo_Internacao", "Custo_Total", "Tipo_Hospital"]
    df_limpo = df.select(*colunas_principais).filter(col("Tempo_Internacao").isNotNull())
    
    # Salvar na camada Silver
    df_limpo.write.mode("overwrite").parquet(silver_path)
    print("Transformação concluída!")

if __name__ == "__main__":
    transformar_dados()
