# Estrutura de Diretórios e Arquivos do Projeto no VS Code.

ds-aih-pipeline
|   .gitignore
|   docker-compose.yaml
|   estrutura.txt
|   LICENSE
|   projeto.md
|   README.md
|   requirements.txt
|   
+---dags
|       aih_pipeline.py
|       
+---data
|   +---bronze
|   +---gold
|   +---raw
|   |   +---csv
|   |   +---dbf
|   |   \---zip
|   |           Arquivos Auxiliares para Tabulação.zip
|   |           Documentação.zip
|   |           SIHSUS_SP_2018_2023.zip
|   |           
|   \---silver
+---imgs
|       tranfer-arquivos-sih-datasus.jpg
|       
+---logs
\---scripts
        ingestion.py
        transformation.py
        
