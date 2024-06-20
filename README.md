
![img](.\img\webscrapping-ibm.png)

## Objetivo

Fomos contratados pela Multiplex, uma empresa de gerenciamento para extrair as informações dos 50 melhores filmes com a melhor classificação média do link compartilhado, para acessar o site [clique aqui](https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films).


## Bibliotecas

Para verificar todas as bibliotecas do projeto, abrir o arquivo requirements.txt

## Como rodar o projeto

1. Clone o repositório:
```bash
git clone https://github.com/LeoGrochoski/web_scraping_and_extracting_data_using_apis.git

cd web_scrapping_and_extracting_data_using_apis
```
2. Configure a versão correta do Python com `pyenv`:
```bash
pyenv install 3.12.1
pyenv local 3.12.1
```
3. Instale as dependências do projeto:
```bash
python -m venv .venv
# O padrao é utilizar .venv
source .venv/bin/activate
# Usuários Windows
pip install -r requirements.txt  
```

4. Rode o projeto
```bash
cd src

python webscrapping_movies.py
```

5. Para verificar funcionamento do banco utilizando select 
```bash
cd sql
python query1.py
```
 

## Documentação completa

Para verificar a documentação detalhada do código e seu funcionamento
acessar [clique aqui](https://leogrochoski.github.io/web_scraping_and_extracting_data_using_apis/)

