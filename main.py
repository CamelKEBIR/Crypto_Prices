#coding-utf8

import pandas_datareader as web
import matplotlib.pyplot as plt
import mplfinance as mpf

import datetime as dt


crypto = "devise souhaité"
currency = "EUR"

 
start = dt.datetime(2021,1,1)
end = dt.datetime.now()

devise souhaité = web.DataReader(f"{crypto}-{currency}", "yahoo" , start, end)  # Autres sources, comme Yahoo ou Alpha Vantage.


#print(data)
# ou 

# affichage graphique > plt.plot(data["Close"])
#plt.show()
# ou 

mpf.plot(devise souhaité, type="candle", volume=True, style="yahoo")
