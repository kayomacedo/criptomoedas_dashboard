## Explicação das Funções Pandas no Código

### Carregando os Dados dos CSVs

```python
bitcoin_df = pd.read_csv('src/datas/bitcoin_2018_2023.csv', index_col='Date', parse_dates=True)
ethereum_df = pd.read_csv('src/datas/ethereum_2018_2023.csv', index_col='Date', parse_dates=True)
dogecoin_df = pd.read_csv('src/datas/dogecoin_2018_2023.csv', index_col='Date', parse_dates=True)
