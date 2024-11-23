# Estrutura de Diretórios e Arquivos do Projeto no VS Code.

<!-- ds-aih-pipeline
├── .gitignore
├── LICENSE
├── README.md
├── dags/
│ └── aih_pipeline.py
├── data/
│ ├── bronze/
│ ├── gold/
│ ├── raw/
│ │ ├── csv/
│ │ ├── dbf/
│ │ └── zip/
│ │ ├── Arquivos Auxiliares para Tabulação.zip
│ │ ├── Documentação.zip
│ │ └── SIHSUS_SP_2018_2023.zip
│ └── silver/
├── docker-compose.yaml
├── docs/
│ └── README.md
├── estrutura.md
├── estrutura.txt
├── imgs/
│ └── tranfer-arquivos-sih-datasus.jpg
├── logs/
├── projeto.md
├── requirements.txt
└── scripts/
├── bronze/
│ └── ingestion.py
├── gold/
│ ├── aggregation.py
│ ├── enrichment.py
│ ├── finalization.py
│ └── formatting.py
└── silver/
└── transformation.py -->

ds-aih-pipeline/
┣📂 dags/
┃ ┗📄 aih_pipeline.py
┣📂 data/
┃ ┣📂 bronze/
┃ ┣📂 gold/
┃ ┣📂 raw/
┃ ┃ ┣📂 csv/
┃ ┃ ┣📂 dbf/
┃ ┃ ┗📂 zip/
┃ ┃ ┣📄 Arquivos Auxiliares para Tabulação.zip
┃ ┃ ┣📄 Documentação.zip
┃ ┃ ┗📄 SIHSUS_SP_2018_2023.zip
┃ ┗📂 silver/
┣📂 docs/
┃ ┗📄 README.md
┣📂 imgs/
┃ ┗📄 tranfer-arquivos-sih-datasus.jpg
┣📂 logs/
┣📂 scripts/
┃ ┣📂 bronze/
┃ ┃ ┗📄 ingestion.py
┃ ┣📂 gold/
┃ ┃ ┣📄 aggregation.py
┃ ┃ ┣📄 enrichment.py
┃ ┃ ┣📄 finalization.py
┃ ┃ ┗📄 formatting.py
┃ ┗📂 silver/
┃ ┗📄 transformation.py
┣📄 .gitignore
┣📄 docker-compose.yaml
┣📄 estrutura.md
┣📄 estrutura.txt
┣📄 LICENSE
┣📄 projeto.md
┣📄 README.md
┗📄 requirements.txt
