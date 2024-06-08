## Explicação das Funções Pandas no Código

### Carregando os Dados dos CSVs

```python
bitcoin_df = pd.read_csv('src/datas/bitcoin_2018_2023.csv', index_col='Date', parse_dates=True)
ethereum_df = pd.read_csv('src/datas/ethereum_2018_2023.csv', index_col='Date', parse_dates=True)
dogecoin_df = pd.read_csv('src/datas/dogecoin_2018_2023.csv', index_col='Date', parse_dates=True)
```
```
pd.read_csv: Carrega os dados de um arquivo CSV para um DataFrame do pandas.
index_col='Date': Define a coluna 'Date' como o índice do DataFrame para facilitar operações baseadas em datas.
parse_dates=True: Converte a coluna 'Date' para o formato datetime, permitindo operações de data e hora.
```
### Calculando o Crescimento Total para Cada Moeda

```python
btc_total_growth = bitcoin_df['Close'].pct_change().sum() * 100
eth_total_growth = ethereum_df['Close'].pct_change().sum() * 100
doge_total_growth = dogecoin_df['Close'].pct_change().sum() * 100
```
```
pct_change(): Calcula a mudança percentual entre os preços de fechamento consecutivos.
sum(): Soma todas as mudanças percentuais para obter o crescimento total ao longo do período.
* 100: Converte a mudança de proporção para uma porcentagem.
```
### Calculando o Crescimento Percentual no Último Ano

```python
btc_recent_growth = bitcoin_df['Close'].pct_change(periods=365).iloc[-1] * 100
eth_recent_growth = ethereum_df['Close'].pct_change(periods=365).iloc[-1] * 100
doge_recent_growth = dogecoin_df['Close'].pct_change(periods=365).iloc[-1] * 100
```

```
pct_change(periods=365): Calcula a mudança percentual ao longo de 365 dias.
iloc[-1]: Seleciona a última entrada do DataFrame para obter a mudança percentual mais recente.
* 100: Converte a mudança de proporção para uma porcentagem.
```
### Calculando a Volatilidade Anual

```python
btc_annual_growth = bitcoin_df['Close'].resample('Y').ffill().pct_change() * 100
eth_annual_growth = ethereum_df['Close'].resample('Y').ffill().pct_change() * 100
doge_annual_growth = dogecoin_df['Close'].resample('Y').ffill().pct_change() * 100
```
```
resample('Y'): Agrupa os dados por ano (YE significa Year-End, ou fim de ano).
ffill(): Preenche os valores ausentes propagando para frente.
pct_change(): Calcula a mudança percentual anual.
* 100: Converte a mudança de proporção para uma porcentagem.
```
### Calculando a Volatilidade (Desvio Padrão)

```python
btc_volatility = btc_annual_growth.std()
eth_volatility = eth_annual_growth.std()
doge_volatility = doge_annual_growth.std()
```
```
std(): Calcula o desvio padrão da série de dados, que representa a volatilidade dos retornos anuais.
```
### Encontrando o Ano de Maior Crescimento

```
idxmax().year: Retorna o ano da entrada máxima na série.
.max(): Retorna o valor máximo da série.
```
## Calculando a Correlação entre as Criptomoedas

```python
crypto_corr = pd.concat([bitcoin_df['Close'], ethereum_df['Close'], dogecoin_df['Close']], axis=1)
crypto_corr.columns = ['Bitcoin', 'Ethereum', 'Dogecoin']

corr_matrix = crypto_corr.pct_change().corr()
```
```
pd.concat([...], axis=1): Concatena os DataFrames ao longo das colunas.
.columns = [...]: Renomeia as colunas do DataFrame resultante.
pct_change(): Calcula a mudança percentual de cada criptomoeda.
corr(): Calcula a matriz de correlação entre as mudanças percentuais.
Essas funções e métodos do pandas são usados para transformar, calcular e analisar os dados históricos das criptomoedas, oferecendo uma visão abrangente do comportamento ao longo do tempo.
```
