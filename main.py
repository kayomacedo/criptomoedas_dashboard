import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados dos CSVs a partir do caminho especificado
bitcoin_df = pd.read_csv('src/datas/bitcoin_2018_2023.csv', index_col='Date', parse_dates=True)
ethereum_df = pd.read_csv('src/datas/ethereum_2018_2023.csv', index_col='Date', parse_dates=True)
dogecoin_df = pd.read_csv('src/datas/dogecoin_2018_2023.csv', index_col='Date', parse_dates=True)

dogcoin_color = "#00ffff"
bitcoin_color ="#ecec53"
eth_color= "#00fa9a"

# Lista de criptomoedas disponíveis
crypto_list = ['Bitcoin', 'Ethereum', 'Dogecoin']


# Melhores momentos de investimento de cada moeda
best_times_to_invest = """
Os melhores momentos para investir em criptomoedas podem ser identificados através da análise histórica e eventos significativos que afetaram o mercado. Aqui estão alguns exemplos:

- **Bitcoin:**
  - **Dezembro de 2020:** O Bitcoin experimentou um aumento significativo de preço devido à crescente adoção institucional e a percepção do Bitcoin como uma reserva de valor alternativa durante a incerteza econômica global.

- **Ethereum:**
  - **Maio de 2021:** Ethereum viu um aumento substancial devido à popularidade dos contratos inteligentes e aplicativos descentralizados (dApps), além do lançamento do Ethereum 2.0.

- **Dogecoin:**
  - **Abril de 2021:** Dogecoin teve picos de preço impulsionados por tweets de figuras públicas influentes e eventos de mídia social.

Esses períodos destacam-se não apenas pelos aumentos de preço, mas também pelos eventos específicos que impulsionaram esses movimentos no mercado de criptomoedas.
"""

# Função para plotar gráfico de linhas
def plot_line_chart(df, crypto_name, column_name, title):
    fig, ax = plt.subplots(figsize=(10, 6))
    for crypto in crypto_name:
        ax.plot(df.index, df[crypto], label=crypto)
    ax.set_xlabel('Data')
    ax.set_ylabel(column_name)
    ax.set_title(title)
    ax.legend()
    return fig, ax

# Calcular crescimento total para cada moeda
btc_total_growth = bitcoin_df['Close'].pct_change().sum() * 100
eth_total_growth = ethereum_df['Close'].pct_change().sum() * 100
doge_total_growth = dogecoin_df['Close'].pct_change().sum() * 100

# Calcular crescimento percentual no último ano
btc_recent_growth = bitcoin_df['Close'].pct_change(periods=365).iloc[-1] * 100
eth_recent_growth = ethereum_df['Close'].pct_change(periods=365).iloc[-1] * 100
doge_recent_growth = dogecoin_df['Close'].pct_change(periods=365).iloc[-1] * 100

# Calcular volatilidade anual
btc_annual_growth = bitcoin_df['Close'].resample('YE').ffill().pct_change() * 100
eth_annual_growth = ethereum_df['Close'].resample('YE').ffill().pct_change() * 100
doge_annual_growth = dogecoin_df['Close'].resample('YE').ffill().pct_change() * 100


btc_volatility = btc_annual_growth.std()
eth_volatility = eth_annual_growth.std()
doge_volatility = doge_annual_growth.std()

# Encontrar o ano de maior crescimento
max_year_btc = btc_annual_growth.idxmax().year
max_growth_btc = btc_annual_growth.max()
max_year_eth = eth_annual_growth.idxmax().year
max_growth_eth = eth_annual_growth.max()
max_year_doge = doge_annual_growth.idxmax().year
max_growth_doge = doge_annual_growth.max()

# Calcular correlação entre as criptomoedas
crypto_corr = pd.concat([bitcoin_df['Close'], ethereum_df['Close'], dogecoin_df['Close']], axis=1)
crypto_corr.columns = ['Bitcoin', 'Ethereum', 'Dogecoin']
corr_matrix = crypto_corr.pct_change().corr()

# Previsões ou tendências futuras (simulado com texto estático)
future_trends = """
Com base nas análises históricas e nas tendências atuais, espera-se que o Bitcoin continue sendo uma das criptomoedas mais promissoras devido à sua alta liquidez e adoção crescente como reserva de valor digital. Ethereum, por sua vez, está se destacando no campo dos contratos inteligentes e aplicativos descentralizados (dApps), enquanto Dogecoin permanece volátil e influenciado por eventos de mídia social e iniciativas comunitárias.
"""

# Criar a dashboard no Streamlit
st.set_page_config(layout="wide", initial_sidebar_state="expanded")
st.title('Análise de Criptomoedas (2018-2023)')

# Mostrar resultados dos cálculos
with st.container():
    col1, col2, col3 = st.columns([1, 1, 1])

    # Mostrar a moeda com maior valorização
    with col1:
        st.subheader('Moeda com Maior Valorização')
        max_growth_coin = max(btc_total_growth, eth_total_growth, doge_total_growth)
        if max_growth_coin == btc_total_growth:
            st.write(f"Bitcoin ({btc_total_growth:.2f}%)")
        elif max_growth_coin == eth_total_growth:
            st.write(f"Ethereum ({eth_total_growth:.2f}%)")
        elif max_growth_coin == doge_total_growth:
            st.write(f"Dogecoin ({doge_total_growth:.2f}%)")

        # Mostrar crescimento percentual no último ano
        st.subheader('Crescimento Percentual no Último Ano')
        st.write(f"Bitcoin: {btc_recent_growth:.2f}%")
        st.write(f"Ethereum: {eth_recent_growth:.2f}%")
        st.write(f"Dogecoin: {doge_recent_growth:.2f}%")

        st.markdown("---")
        # Mostrar previsões ou tendências futuras
        st.subheader('Previsões ou Tendências Futuras')
        st.write(future_trends)
        st.markdown("---")

    # Mostrar a moeda com menor valorização
    with col2:
        st.subheader('Moeda com Menor Valorização')
        min_growth_coin = min(btc_total_growth, eth_total_growth, doge_total_growth)
        if min_growth_coin == btc_total_growth:
            st.write(f"Bitcoin ({btc_total_growth:.2f}%)")
        elif min_growth_coin == eth_total_growth:
            st.write(f"Ethereum ({eth_total_growth:.2f}%)")
        elif min_growth_coin == doge_total_growth:
            st.write(f"Dogecoin ({doge_total_growth:.2f}%)")

    # Mostrar gráfico de barras com crescimento total
    with col3:
        # Mostrar crescimento percentual total em um gráfico de barras
        st.subheader('Crescimento Percentual Total')
        fig_growth_total, ax_growth_total = plt.subplots(figsize=(8, 3))
        bars = ax_growth_total.bar(crypto_list, [btc_total_growth, eth_total_growth, doge_total_growth], color=[bitcoin_color, eth_color, dogcoin_color])
        ax_growth_total.set_xlabel('Criptomoeda', color='white')
        ax_growth_total.set_ylabel('Crescimento Total (%)', color='white')
        ax_growth_total.set_title('Crescimento Percentual Total das Criptomoedas', color='white')

        # Mudar cor de fundo do gráfico
        fig_growth_total.patch.set_facecolor('#272530')  # Escolha a cor de fundo desejada

        # Mudar as cores dos textos nos eixos
        ax_growth_total.tick_params(axis='x', colors='white')
        ax_growth_total.tick_params(axis='y', colors='white')

        # Mudar as cores das bordas das barras
        for bar in bars:
            if bar.get_x() == 0:  # Índice da barra do Bitcoin (ajuste conforme necessário)
                bar.set_edgecolor('black')  # Cor da borda da barra do Bitcoin
                bar.set_linewidth(2)  # Largura da borda
            else:
                bar.set_edgecolor('black')  # Cor da borda das outras barras
                bar.set_linewidth(2)  # Largura da borda

        # Mostrar o gráfico no Streamlit
        st.pyplot(fig_growth_total)


with st.container():
    col1, col2,col3 = st.columns([2.2,1,1])
    # Mostrar gráficos dinâmicos de linhas para Preço de Fechamento das Criptomoedas selecionadas

    with col1:

        def plot_line_chart(df, crypto_name, column_name, title):
            fig, ax = plt.subplots(figsize=(15, 6))
            colors = [bitcoin_color, eth_color, dogcoin_color]  # Defina suas cores personalizadas aqui
            for i, crypto in enumerate(crypto_name):
                ax.plot(df.index, df[crypto], label=crypto, color=colors[i])
            ax.set_xlabel('Data', color='white')  # Cor do texto do eixo x
            ax.set_ylabel(column_name, color='white')  # Cor do texto do eixo y
            ax.set_title(title, color='white')  # Cor do título
            ax.legend()

            # Mudar cor de fundo do gráfico
            fig.patch.set_facecolor('#272530')  # Escolha a cor de fundo desejada

            # Mudar as cores dos textos nos eixos
            ax.tick_params(axis='x', colors='white')
            ax.tick_params(axis='y', colors='white')

            # Mudar a cor da legenda
            legend = ax.legend()
            for text in legend.get_texts():
                text.set_color('black')

            return fig, ax

        # Usando as cores personalizadas no gráfico
        st.subheader('Preço de Fechamento das Criptomoedas')
        fig_close_price, ax_close_price = plot_line_chart(crypto_corr, crypto_list, 'Close', 'Preço de Fechamento das Criptomoedas')
        st.pyplot(fig_close_price)
            

    with col3:
         # Exibir lista de crescimentos percentuais com fundo colorido
        st.text("Criptomoedas")
        html_content = """
        <ul style="background-color: #272530; padding: 10px; border-radius: 5px; color: white;">
            <li> 🥇 Bitcoin</li>
            <li>🥈 Ethereum</li>
            <li>🥉 Dogecoin</li>
            
        """

        # Exibir no Streamlit
        st.markdown(html_content, unsafe_allow_html=True)
    
    with col3:
        # Mostrar volatilidade anual em um gráfico de pizza
        st.subheader('Volatilidade Anual')
        fig_volatility, ax_volatility = plt.subplots(figsize=(4, 6))
        ax_volatility.pie([btc_volatility, eth_volatility, doge_volatility], labels=crypto_list, autopct='%1.1f%%', startangle=140, colors=[bitcoin_color, eth_color, dogcoin_color])
        ax_volatility.axis('equal')
        ax_volatility.set_title('Volatilidade Anual das Criptomoedas', color='white')

        # Mudar as cores dos textos dentro do gráfico
        for i, text in enumerate(ax_volatility.texts):
            if 'Bitcoin' in text.get_text():
                text.set_color('white')  # Mudar a cor do texto do Bitcoin para preto
            elif "Ethereum" in text.get_text():
                text.set_color('white')
                
            elif "Dogecoin" in text.get_text():
                text.set_color('white')
            else:
                text.set_color('black')  # Manter a cor do texto dos outros elementos

        # Mudar cor de fundo do gráfico
        fig_volatility.patch.set_facecolor('#272530')  # Escolha a cor de fundo desejada

        # Mostrar o gráfico no Streamlit
        st.pyplot(fig_volatility)


 

with st.container():
    col1,col2,col3 = st.columns([1,0.2,2.2])
        # Mostrar correlação entre as criptomoedas usando seaborn em um heatmap

    with col1:
        st.markdown(""" 

""")
        st.subheader('Correlação')
        st.markdown("""
        A correlação entre criptomoedas é uma medida estatística que descreve como os preços das criptomoedas se movem em relação umas às outras ao longo do tempo.

        - **Correlação positiva (próxima de +1)**: Indica que os preços das criptomoedas tendem a se mover na mesma direção.
        - **Correlação negativa (próxima de -1)**: Indica que os preços das criptomoedas tendem a se mover em direções opostas.
        - **Correlação próxima de 0**: Indica que não há relação linear entre os movimentos dos preços das criptomoedas.

        O heatmap abaixo mostra visualmente a matriz de correlação entre Bitcoin, Ethereum e Dogecoin com base nas variações percentuais de preço.
        """)



    with col3:
        st.subheader('Correlação entre Criptomoedas')
        fig_corr, ax_corr = plt.subplots(figsize=(15, 6))

        # Configurar o heatmap com anotações coloridas
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, ax=ax_corr, annot_kws={"color": "white"})

        # Ajustar o título do gráfico
        ax_corr.set_title('Correlação entre Criptomoedas', color='white')

        # Mudar a cor de fundo do gráfico
        fig_corr.patch.set_facecolor('#272530')

        # Mudar as cores dos textos dos eixos
        ax_corr.tick_params(axis='x', colors='white')
        ax_corr.tick_params(axis='y', colors='white')

        # Mostrar o gráfico no Streamlit
        st.pyplot(fig_corr)

# Adicionando o texto à sua dashboard
with st.container():
    col1,col2,col3 = st.columns([1,2,1])
    with col2:
        st.markdown(
            """
            <div style="padding: 10px; padding-top:50px;  border-radius: 30px; text-align: center;">
                
            </div>
            """,
            unsafe_allow_html=True
        )
        with st.container():
            col1,col2,col3 = st.columns([1,1,1])
          
            with col2:
                st.image("src/logo.png", caption="Cripto", width=200)
                
       
        
        st.subheader('Quais foram Melhores Momentos para Investir em Criptomoedas?')
        st.write(best_times_to_invest)
       