#coding-utf8

import pandas_datareader as web
import matplotlib.pyplot as plt
import mplfinance as mpf

import datetime as dt


crypto = "ETH"
currency = "EUR"

 
start = dt.datetime(2021,1,1)
end = dt.datetime.now()

ETH = web.DataReader(f"{crypto}-{currency}", "yahoo" , start, end)  # Other sources, like yahoo and Alpha Vantage, do function.


#print(data)
# ou 

# affichage graphique > plt.plot(data["Close"])
#plt.show()
# ou 

mpf.plot(ETH, type="candle", volume=True, style="yahoo")