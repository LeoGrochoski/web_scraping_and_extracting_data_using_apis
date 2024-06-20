# Extração de Dados da Web

Web scraping é usado para extração de dados relevantes de páginas da web. Se você precisar de alguns dados de uma página da web de domínio público, o web scraping torna o processo de extração de dados bastante conveniente. 

O uso de web scraping, entretanto, requer algum conhecimento básico da estrutura das páginas HTML. Neste projeto, demonstrarei o processo de análise do código HTML de uma página da web e como extrair as informações necessárias dela usando web scraping em Python.

## Dados

|Filme|Ano|Avaliação Rotten Tomatoes|
|-----|---|-------------------------|
|The Godfather|1972|17|
|Citizen Kane|1941|2|
|Casablanca|1942|8|
|"The Godfather, Part II"|1974|99|
|Singin' in the Rain|1952|52|
|Psycho|1960|88|
|Rear Window|1954|47|
|Apocalypse Now|1979|unranked|
|2001: A Space Odyssey|1968|unranked|
|Seven Samurai|1954|49|
|Vertigo|1958|unranked|
|unset Blvd|1950|21|
|Modern Times|1936|4|
|Lawrence of Arabia|1962|unranked|
|North by Northwest|1959|79
|Star Wars|1977|unranked|
|Parasite|2019|6|
|Schindler's List|1993|unranked|
|Lord of the Rings: The Fellowship of the Ring|2001|unranked|
|Shawshank Redemption|1994|unranked|
|It's a Wonderful Life|1946|unranked|
|Pulp Fiction|1994|unranked|
|Avengers: Endgame|2019|7|
|City Lights|1931|unranked|
|One Flew Over the Cuckoo's Nest|1975|unranked|


## Funções

load_webpage()
::: src.webscrapping_movies.load_webpage
find_tables()
::: src.webscrapping_movies.find_tables
transform_data()
::: src.webscrapping_movies.transform_data
save_db()
:::src.webscrapping_movies.save_db


