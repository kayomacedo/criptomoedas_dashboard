## Explicação das Funções Pandas no Código

### Carregando os Dados dos CSVs

```python
bitcoin_df = pd.read_csv('src/datas/bitcoin_2018_2023.csv', index_col='Date', parse_dates=True)
ethereum_df = pd.read_csv('src/datas/ethereum_2018_2023.csv', index_col='Date', parse_dates=True)
dogecoin_df = pd.read_csv('src/datas/dogecoin_2018_2023.csv', index_col='Date', parse_dates=True)

pd.read_csv: Carrega os dados de um arquivo CSV para um DataFrame do pandas.
index_col='Date': Define a coluna 'Date' como o índice do DataFrame para facilitar operações baseadas em datas.
parse_dates=True: Converte a coluna 'Date' para o formato datetime, permitindo operações de data e hora.
Calculando o Crescimento Total para Cada Moeda

btc_total_growth = bitcoin_df['Close'].pct_change().sum() * 100
eth_total_growth = ethereum_df['Close'].pct_change().sum() * 100
doge_total_growth = dogecoin_df['Close'].pct_change().sum() * 100
