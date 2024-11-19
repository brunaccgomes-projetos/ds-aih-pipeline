# ds-aih-pipeline
Desenvolvimento de uma pipeline robusta de dados para ingestão e transformação de grandes volumes de dados de internações hospitalares (AIH - Autorização de Internação Hospitalar) do DATASUS.

## Documentos
- Escopo Inicial
- Fase 1: Planejamento da Pipeline de Dados
- Fase 2: Elaboração de Scripts Iniciais

## Estrutura de Diretórios Local
ds-aih-pipeline/
│
├── scripts/                # Scripts de código-fonte
│   ├── ingestion.py        # Script para ingestão de dados (Azure)
│   ├── transformation.py   # Script para transformações (Spark)
│   ├── utils.py            # Funções utilitárias compartilhadas
│
├── docker/                 # Configurações para containerização
│   ├── Dockerfile          # Configuração de imagem Docker
│   ├── requirements.txt    # Dependências Python
│
├── configs/                # Configurações externas e credenciais (NÃO SUBIR AO GIT!)
│   ├── azure_config.json   # Configurações do Azure Data Lake
│   ├── spark_config.json   # Configurações do Apache Spark
│
├── temp/                   # Dados temporários baixados/local
│   ├── ...
│
├── tests/                  # Scripts de teste
│   ├── test_ingestion.py   # Testes para o script de ingestão
│   ├── test_transformation.py
│
├── README.md               # Documentação do projeto
└── .gitignore              # Arquivos a serem ignorados no Git
