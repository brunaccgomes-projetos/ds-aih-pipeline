# ds-aih-pipeline
Desenvolvimento de uma pipeline robusta de dados para ingestão e transformação de grandes volumes de dados de internações hospitalares (AIH - Autorização de Internação Hospitalar) do DATASUS.

# Projeto
- Escopo Inicial para AIH1
      1. Definir o Período de Análise
      2. Variáveis de Interesse
      3. Objetivos Analíticos Focados
      4. Dados Complementares (Opcional)
- Primeiras Etapas
      - Ingestão
      - Processamento
      - Resultados Simples
- Fase 1: Planejamento da Pipeline de Dados
      - 1. Estrutura da Pipeline
      - 2. Componentes e Ferramentas
      - 3. Variáveis Inicialmente Selecionadas
- Fase 2: Elaboração de Scripts Iniciais
      - 1. Script para Ingestão de Dados
      - 2. Componentes e Ferramentas
  

<a id="ancora1"></a>
## Escopo Inicial para AIH
**1. Definir o Período de Análise:**
- Escolher um intervalo de 3 a 5 anos (2018 a 2023).
- Dados limitados pelo estado de São Paulo para reduzir o volume inicial.

**2. Variáveis de Interesse:**
- Diagnóstico principal (CID).
- Procedimentos realizados.
- Duração da internação.
- Custos da internação.
- Tipo de hospital (público ou privado).

**3. Objetivos Analíticos Focados:**
- Identificar os diagnósticos mais frequentes por tipo de hospital e região.
- Analisar os custos médios por tipo de internação.
- Avaliar a evolução do tempo médio de internação para doenças crônicas.

**4. Dados Complementares (Opcional):**
- Tabelas de referências do DATASUS, como códigos CID e procedimentos.

## Primeiras Etapas
**Ingestão:**
- Baixar os dados da AIH do DATASUS (formato CSV ou DBF).
- Ingestão inicial para Azure Data Lake (camada Bronze).

**Processamento:**
- Padronizar e limpar os dados no Apache Spark.
- Estruturar tabelas analíticas para facilitar consultas.

**Resultados Simples:**
- Criar uma tabela básica com os diagnósticos mais frequentes e custos associados.

## Fase 1: Planejamento da Pipeline de Dados
### Etapas
**1. Estrutura da Pipeline:**
  - Camada de Ingestão:
      - Baixar os dados de AIH do DATASUS para a camada "Bronze" do Azure Data Lake.
  - Camada de Processamento:
      - Limpar, padronizar e transformar os dados utilizando Apache Spark.
  - Camada de Análise:
      - Criar tabelas analíticas (camada "Gold") prontas para consumo por ferramentas de visualização e análises.
   
**2. Componentes e Ferramentas:**
  - Azure Data Lake: Armazenamento em camadas (Bronze, Silver e Gold).
  - Apache Spark: Processamento distribuído de dados.
  - Airflow: Orquestração das tarefas da pipeline.
  - Docker: Criação de containers para padronizar ambientes.
  - SQL: Para consultas e agregações durante a transformação.
  
**3. Variáveis Inicialmente Selecionadas:**
  - Diagnósticos (CID principal e secundário).
  - Tempo de internação.
  - Custo total da internação.
  - Tipo de hospital (público ou privado).
  - Data de admissão e alta.

## Fase 2: Elaboração de Scripts Iniciais
**1. Script para Ingestão de Dados:**
  - O script buscará arquivos CSV disponíveis no DATASUS e os carregará para a camada Bronze do Azure Data Lake.
  - Código Python para Ingestão: [scripts/ingestion.py](scripts/ingestion.py)

**2. Script para Transformação (Camada Silver):**
  - Após a ingestão, o próximo passo será usar o Apache Spark para limpar e padronizar os dados.
  - Tarefa Inicial com Spark
  - Objetivo: Filtrar colunas principais, remover registros inválidos e salvar como Parquet.
  - Código Python para Transformação: [scripts/transformation.py](scripts/transformation.py)

