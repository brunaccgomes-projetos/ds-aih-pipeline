# 🏥 Projeto de Engenharia de Dados na Saúde no Brasil

Desenvolvimento de uma pipeline de dados para ingestão e transformação de grandes volumes de dados de internações hospitalares (AIH - Autorização de Internação Hospitalar) do DATASUS.

---

## 💻 Especificação Técnica

- IDE: VSCode (Visual Studio Code)
- Linguagem: Python
  - Bibliotecas (principais): boto3, pyspark
- OS: Windows 11

## 🛠️ Componentes e Ferramentas:

- AWS S3: Armazenamento em camadas (Bronze, Silver e Gold).
- Apache Spark: Processamento distribuído de dados.
- Airflow: Orquestração das tarefas da pipeline.
- Docker: Criação de containers para padronizar ambientes.
- SQL: Para consultas e agregações durante a transformação.

## 🚀 Configuração e Execução

### 1. Criar o Ambiente Virtual

1.1. Abra o terminal ou o PowerShell no Windows.

1.2. Navegue até o diretório base do projeto:

`cd D:\GitHub\ds-aih-pipeline`

1.3. Crie o ambiente virtual:

`python -m venv venv`

1.4. Ative o ambiente virtual:

`venv\Scripts\activate`

### 2. Instalar as Dependências

2.1. Instalar as Dependências do arquivo requirements.txt existente:

`pip install -r requirements.txt`

2.2. OU NÃO EXISTE o arquivo requirements.txt:

2.2.1. Primeiro: Instale as dependências necessárias com pip:

Instalando Extras e Operadores Adicionais: - Se você precisar de operadores adicionais, como para integração com o AWS, ajuste o comando para incluir o extra [aws]. - O extra [aws] inclui bibliotecas úteis para conectar ao S3 ou outros serviços da AWS.

```bash
# por uma única linha
pip install pandas pyspark boto3 apache-airflow apache-airflow[aws]
```

```bash
# linha por linha
pip install pandas
pip install pyspark
pip install boto3
pip install apache-airflow
pip install apache-airflow[aws]
```

2.2.2. Segundo: Gere arquivo requirements.txt

`pip freeze > requirements.txt`

### 3. Executar o Script

3.1. Navegue até o diretório onde está o script:

`cd D:\GitHub\ds-aih-pipeline\scripts`

3.2. Execute o script de ingestion com o Python:

`python ingestion.py`

### 4. Manutenção do Ambiente

4.1. Para Desativar o Ambiente:
Quando terminar de usar o ambiente virtual, você pode desativá-lo com o comando:

`deactivate`

4.2. Para Reativar o Ambiente:
Sempre que quiser executar novamente, reative o ambiente com:

`venv\Scripts\activate`

## :bookmark_tabs: Url Download

https://datasus.saude.gov.br/transferencia-de-arquivos/#

![alt text](imgs/tranfer-arquivos-sih-datasus.jpg)

