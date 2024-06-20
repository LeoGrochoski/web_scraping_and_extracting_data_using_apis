import pandas as pd
import sqlite3


db_path: str = '../db/Movies.db'
query_statement = 'SELECT * FROM Top_50'


def select_table(db, query):
    """
    Função para rodar a query de busca da tabela no banco sqlite e nos retorna um Dataframe

    Args: 
        db (str): Trata-se do path do banco
        query (str): Trata-se da query de consulta utilizada como parametro, no caso utilizamos um select simples
    """
    sql_connection = sqlite3.connect(db)
    df = pd.read_sql(query, sql_connection)
    return df


tabela = select_table(db_path, query_statement)
print(tabela)