## PROJETO DE ETL - ELEFLOW - BIGDATA AIRLINES

### Projeto criado para o processo seletivo de engenheiro de dados Jr na eleflow.

#### OBS:
##### Existe o executável do SqliteStudio e o arquivo de banco de dados no repositório, dentro da pasta database para representação prática das tabelas criadas caso necessário. Um pequeno banco de dados foi criado via sqlite.
##### Os notebooks se encontram na pasta ./src/ETL e os csvs após transformação em ./database_files.

### Extras:
##### Foi utilizado Python puro no projeto junto do Pandas, porém, o ideal para a ingestão incremental dos dados mensalmente seria o uso de alguma tecnologia de processamento distruibuido como o Spark, utilizando o Pyspark para realizar o de ETL ou ELT e disponibilizando os dados em buckets de um provedor Cloud. Até utilizei o PySpark nos arquivos json, porém o meu cluster local estava impedindo a execução dos scripts e optei em não gastar mais tempo do que já foi gasto resolvendo esta questão, dato este fato, recorri ao Pandas.
##### As camadas utilizadas neste projeto foram a raw(armazenando os arquivos localmente), e após o processo de transformação, uma camada silver(Dados disponibilizados em formato csv e no banco de dados sqlite em forma de tabelas), e, posteriormente, em forma de views específicas.

### Tecnologias utilizadas:
    - Python
    - SQL
    - Sqlite
    - SqliteStudio
    - Jupyter
    - json
    - csv
    - VsCode
