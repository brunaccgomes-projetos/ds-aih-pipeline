## **Escopo do Projeto de Engenharia de Dados na Saúde no Brasil**

- [💡 **Contexto do Negócio**](#-contexto-do-negócio)
- [🎯 **Objetivos do Projeto**](#-objetivos-do-projeto)
- [🎛 **Principais Requisitos Técnicos**](#-principais-requisitos-técnicos)
- [🛠 **Etapas do Projeto**](#-etapas-do-projeto)
    - [**1. Ingestão de Dados**](#1-ingestão-de-dados)
    - [**2. Armazenamento de Dados**](#2-armazenamento-de-dados)
    - [**3. Processamento e Transformação**](#3-processamento-e-transformação)
    - [**4. Modelagem Analítica e Curadoria**](#4-modelagem-analítica-e-curadoria)
    - [**5. Monitoramento e CI/CD**](#5-monitoramento-e-cicd)
- [🏆 **Resultados Esperados**](#-resultados-esperados)

### 💡 **Contexto do Negócio**

O projeto visa melhorar a eficiência na análise e utilização de dados do Sistema Único de Saúde (SUS) para identificar padrões em internações hospitalares, prevenir complicações em pacientes crônicos e otimizar recursos de saúde. A plataforma será criada para ingestão, transformação, análise e disponibilização de dados de saúde pública, com foco em democratizar o acesso a dados para pesquisadores e gestores.

----------

## 🎯 **Objetivos do Projeto**

1.  **Desenvolver uma pipeline robusta de dados** para ingestão e transformação de grandes volumes de dados de saúde pública, com foco nos sistemas do SUS.
2.  **Analisar internações e tratamentos** para identificar padrões que podem auxiliar na prevenção de complicações em doenças crônicas como diabetes e hipertensão.
3.  **Facilitar a tomada de decisão** ao entregar dados prontos para uso em modelos analíticos e dashboards interativos.
4.  **Garantir escalabilidade e confiabilidade** por meio de uma arquitetura moderna utilizando contêineres e serviços gerenciados em nuvem.

----------

## 🎛 **Principais Requisitos Técnicos**

-   **Docker**: Criação de imagens para pipelines de ingestão e transformação.
-   **Airflow**: Agendamento e monitoramento de tarefas.
-   **Apache Spark**: Processamento distribuído de grandes volumes de dados.
-   **SQL**: Consultas para transformar e preparar dados.
-   **AWS S3**: Armazenamento escalável e seguro.
-   **EKS**: Orquestração de containers para alta disponibilidade.
-   **CI/CD**: Deploy automatizado de mudanças no código.

----------

## 🛠 **Etapas do Projeto**

### **1. Ingestão de Dados**

-   **Origem dos dados**:
    -   Arquivos CSV, JSON e Parquet disponíveis no DATASUS e em portais estaduais de saúde.
    -   Dados de APIs públicas do SUS e outros órgãos relacionados.
-   **Ferramentas e Tecnologias**:
    -   **Python**: Scripts para ingestão inicial e manipulação dos dados.
    -   **Airflow**: Agendador de tarefas para automação do processo de ingestão.
    -   **Docker**: Criação de containers para executar serviços de ingestão de forma isolada.

### **2. Armazenamento de Dados**

-   **Estratégia de armazenamento**:
    -   Dados brutos: Salvos no **AWS S3** em camadas (Bronze).
    -   Dados processados: Após ETL, armazenados nas camadas Silver e Gold.
    -   Compatível com processamento distribuído no **Apache Spark**.
-   **Organização**:
    -   Diretórios segmentados por estado, tipo de dado e ano.
    -   Metadados gerenciados em um catálogo de dados no **AWS Glue**.

### **3. Processamento e Transformação**

-   **Pipeline de ETL**:
    -   Transformação e limpeza dos dados no **Apache Spark**.
    -   Uso de SQL para padronizar nomenclaturas e realizar agregações (ex.: sumarização de internações por tipo de hospital e município).
    -   Implementação de tarefas distribuídas para alta performance.
-   **Ferramentas e Tecnologias**:
    -   **Airflow** para orquestração.
    -   **Docker** e **Kubernetes** para execução em clusters.
    -   **Python** para validação e criação de scripts auxiliares.

### **4. Modelagem Analítica e Curadoria**

-   **Modelagem**:
    -   Desenvolvimento de tabelas analíticas (fatos e dimensões).
    -   Organização no formato estrela ou floco de neve, dependendo da necessidade analítica.
-   **Entrega**:
    -   Dados otimizados para dashboards Power BI ou Tableau.
    -   Exportação de datasets para cientistas de dados via APIs.

### **5. Monitoramento e CI/CD**

-   **Monitoramento**:
    -   Implementação de monitoramento com métricas de sucesso/falha das pipelines (ex.: logs de execução no Airflow e Spark UI).
    -   Alertas em casos de falha de execução.
-   **CI/CD**:
    -   Criação de pipelines de entrega contínua para scripts de ETL e imagens Docker.
    -   Deploy automatizado em clusters **EKS (Amazon Elastic Kubernetes Service)**.
    -   Uso de ferramentas como **GitHub Actions** ou **Azure DevOps**.

----------

## 🏆 **Resultados Esperados**

1.  **Dados limpos e organizados**: Acessíveis em um formato escalável e pronto para análise.
2.  **Insights de saúde pública**: Identificação de padrões críticos para melhorar o atendimento em doenças crônicas.
3.  **Otimização de custos em saúde**: Suporte a políticas públicas com base em evidências extraídas dos dados.
4.  **Sustentabilidade tecnológica**: Infraestrutura modular e escalável para expansão futura.

----------

