import pandas as pd
import requests
import sqlite3
from bs4 import BeautifulSoup
from pandas import DataFrame

# Declração de variaveis, url, nome do banco, nome da tabela, caminho do csv e contador. 

url: str = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
db_name: str = 'Movies.db'
table_name: str = 'Top_50'
csv_path: str = '/C:/Lab/web_scraping_and_extracting_data_using_apis/data/top_50_films.csv'

def load_webpage(url: str):
    """
    Função para carregar a pagina da web deseja para realizar o web scrapping

    1. Utiliza a biblioteca requests passando a url como parametro

    2. Utiliza a biblioteca BeautifulSoup para retornar o html parseado da pagina.

    Args:
        url (str): url do site que iremos realizar o web scrapping.

    Returns:
        data (str): Retorna o html da pagina parseado.
    """
    site: str = requests.get(url).text
    data: str = BeautifulSoup(site, 'html.parser')
    return data

def find_tables(data: str):
    """
    Função para receber o HTML iterar sobre os dados e retornar um dataframe das colunas e linhas desejadas
    
    1. Itera sobre o conteudo da variavei rows(linhas).

    2. Checa pelo contador do loop for para restringir a 50 entradas.

    3. Extrai todos os objetos 'td' na linha e salva na variavel col.

    4. Checa se o tamanho da variavel col é 0. se não houver dados na linha atual. O passo é importante desde que muitas vezes que a linhas que não são aparentes na internet. 
    
    5. Cria um dicionario com a variavel data_dict com as vhaves mesmo que as colunas do DataFrame foram criadas para gravar a saida e os valores das 3 colunas.
    
    6. Converte o dicionario em um dataframe e concatena em um dicionario existente. Dessa forma os dados são incluidos continuamente cada vez que ha uma iteração no loop.
    
    7. Incrementa o contador do loop.
    
    8. Uma vez que o contado atinge a marca de 50, a iteração é interrompida sobre as linhas e o loop é quebrado.    
    
    Args:
        data (str): HTML da pagina web.

    Returns:
        df (str): Retorna um dataframe contendo os 50 primeiros filmes com seu rank medio, nome e ano de lançamento.
    """
    df: DataFrame = pd.DataFrame(columns=["Average Rank","Film","Year"])
    count: int = 0
    tables = data.find_all('tbody')
    rows = tables[0].find_all('tr')
    for row in rows:
        if count<50:
            col = row.find_all('td')
            if len(col)!=0:
                data_dict: dict = {"Average Rank": col[0].contents[0],
                            "Film": col[1].contents[0],
                            "Year": col[2].contents[0]}
                df1: DataFrame = pd.DataFrame(data_dict, index=[0])
                df: DataFrame = pd.concat([df,df1], ignore_index=True)
                count+=1
        else:
            break
    return df 


dados = load_webpage(url)
tabela_dados = find_tables(dados)

# Convertendo DataFrame para HTML para incluir na documentação
df_html: str = tabela_dados.to_html(index=False)

# Salvando HTML em um arquivo
with open('docs/dataframe.html', 'w', encoding='utf-8') as f:
    f.write(df_html)