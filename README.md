# Rick and Morty API - Backend Case

## Objetivo
Consumir a API REST pública Rick and Morty e gerar um arquivo CSV contendo informações de 50 personagens.

## Tecnologias utilizadas
- Python 3
- Requests
- CSV

## Como executar

1. Instale as dependências:
pip install -r requirements.txt

2. Execute o script:
python main.py


3. O arquivo `characters.csv` será gerado automaticamente.

## API utilizada
https://rickandmortyapi.com/api/character

## Formato do CSV
id; name; status; species; type; gender

## Estratégia
Foi utilizada paginação da API (page=1,2,3) para obter pelo menos 50 personagens.
Os dados foram tratados e exportados utilizando delimitador ponto e vírgula (;).
