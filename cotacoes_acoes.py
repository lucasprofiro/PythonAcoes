import pandas as pd
import numpy as np
from pandas_datareader import data as web


def cotacoes_acoes(tickers=['^BVSP'],dataInicio='01/01/2021'):
    """Baixa todos os dados de fechamento de mercado passando os tickers em
    lista e a data de inicio no formato mm/dd/aaaa
    Como padrão: Ínidce Bovespa e 01/01/2021
    Consultar o nome dos tickers no site do Yahoo"""
    
    #Garantindo todos os tickers em maiusculo
    tickers = [x.upper() for x in tickers]
    
    prices = pd.DataFrame()
    
    for i in tickers:
        if '^BVSP' in i:
            prices[i] = web.get_data_yahoo(i,dataInicio)['Adj Close']
        elif '.SA' in i:
            prices[i] = web.get_data_yahoo(i,dataInicio)['Adj Close']
        else:
            i = i+'.SA'
            prices[i] = web.get_data_yahoo(i,dataInicio)['Adj Close']
    
    #arredondar os valores para 2 casas decimais
    prices = np.round(prices, decimals=2)
    
    if "^BVSP" in tickers:
        prices['^BVSP'] = prices['^BVSP']/1000

    return prices



#exemplos
a1 = cotacoes_acoes(['enbr3'])
a2 = cotacoes_acoes(['enbr3.sa'])
a7 =cotacoes_acoes(['enbr3.sa','petr4','^bvsp'])
a3 = cotacoes_acoes(['enbr']) #errado, pois está sem o 3
a4 = cotacoes_acoes(['petr4.sa'])
a5 = cotacoes_acoes(['petr3.sa'])
a6 =cotacoes_acoes(['^bvsp'])
