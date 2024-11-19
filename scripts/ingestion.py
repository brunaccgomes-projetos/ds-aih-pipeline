import os
import requests
from azure.storage.blob import BlobServiceClient

# Configurações iniciais
AZURE_CONNECTION_STRING = "sua_chave_de_conexão"
CONTAINER_NAME = "bronze-dados"
BASE_URL = "https://datasus.saude.gov.br/arquivos/aih"  # Exemplo fictício, ajuste conforme o real
ANOS = range(2018, 2024)
ESTADO = "SP"

def download_dados_aih(ano, estado, output_dir):
    """
    Baixa os dados da AIH para um diretório local.
    """
    url = f"{BASE_URL}/aih_{ano}_{estado}.csv"
    response = requests.get(url)
    if response.status_code == 200:
        output_path = os.path.join(output_dir, f"aih_{ano}_{estado}.csv")
        with open(output_path, "wb") as f:
            f.write(response.content)
        print(f"Arquivo salvo: {output_path}")
        return output_path
    else:
        print(f"Falha no download: {url}")
        return None

def upload_to_azure(blob_service_client, container_name, file_path):
    """
    Faz o upload de um arquivo local para o Azure Data Lake.
    """
    blob_name = os.path.basename(file_path)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)
    print(f"Upload concluído: {blob_name}")

def main():
    # Diretório temporário para salvar arquivos
    temp_dir = "./temp"
    os.makedirs(temp_dir, exist_ok=True)
    
    # Conexão com Azure
    blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
    
    for ano in ANOS:
        file_path = download_dados_aih(ano, ESTADO, temp_dir)
        if file_path:
            upload_to_azure(blob_service_client, CONTAINER_NAME, file_path)
    
    # Limpeza dos arquivos temporários
    for f in os.listdir(temp_dir):
        os.remove(os.path.join(temp_dir, f))
    print("Processo finalizado!")

if __name__ == "__main__":
    main()
