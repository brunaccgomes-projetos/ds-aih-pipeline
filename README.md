## Especificação Técnica

- **IDE:** VSCode (Visual Studio Code)
- **Linguagem:** Python
  - **Bibliotecas (principais):** boto3, pyspark

## Configuração e Execução

### 1. Criar o Ambiente Virtual

- **1.1. Abra o terminal ou o PowerShell no Windows.**

- **1.2. Navegue até o diretório base do projeto:**
  cd D:\GitHub\ds-aih-pipeline

- **1.3. Crie o ambiente virtual:**
  python -m venv venv

- **1.4. Ative o ambiente virtual:**
  venv\Scripts\activate

### 2. Instalar as Dependências

- **2.1. Instale as dependências do arquivo requirements.txt existente**
  pip install -r requirements.txt

- **2.2. OU CASO exclua o arquivo requirements.txt existente:**

  - **2.2.1. Primeiro: Instale as dependências necessárias com pip:**
    pip install pyspark
    pip install boto3

  - **2.2.2. Segundo: Gere arquivo requirements.txt**
    pip freeze > requirements.txt

### 3. Executar o Script

- **3.1. Navegue até o diretório onde está o script:**
  cd D:\GitHub\ds-aih-pipeline\scripts

- **3.2. Execute o script de ingestion com o Python:**
  python ingestion.py

### 4. Manutenção do Ambiente

- **4.1. Para Desativar o Ambiente:**
  **Quando terminar de usar o ambiente virtual, você pode desativá-lo com o comando:**
  deactivate

- **4.2. Para Reativar o Ambiente:**
  **Sempre que quiser executar novamente, reative o ambiente com:**
  venv\Scripts\activate
