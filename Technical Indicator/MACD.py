from curses import window
import numpy as np
# import pandas as pd
# import yfinance as yf
# import matplotlib.pyplot as plt

df= 
# df.to_csv('tesla.csv')

def macdIndictor(df):
    df['SMA20']= df.Close.rolling(window = 20).mean()
    df['SMA50'] = df.Close.rolling(window =50).mean()
    df['SMA200'] = df.Close.rolling(window =200).mean()
    df['EMA20'] = df.Close.ewm(span =20).mean()
    df['EMA50'] = df.Close.ewm(span =20).mean()
    df['EMA12']= df.Close.ewm(span=12).mean()
    df['EMA26'] = df.Close.ewm(span =26).mean()
    df['MACD1'] = df.EMA12- df.EMA26
    df['SIGNAL']= df.MACD1.ewm(span=9).mean()

    df['MACD'] = np.where(df.MACD1>df.SIGNAL,'UP','Down')
    #RSI
    RSI_PERIOD = 14  
    df['Change'] = df.Close.diff()
    df['Up'] = df['Change'].apply(lambda x: x if x>0 else 0)
    df['Down'] =df['Change'].apply(lambda x:x if x<0 else 0)
    df['avg Up'] = df['Up'].ewm(span = RSI_PERIOD-1).mean()
    df['avg Down'] = df['Down'].ewm(span = RSI_PERIOD-1).mean()
    df = df.dropna()
    df['RS']  = abs(df.loc[:,'avg Up']/df.loc[:,'avg Down'])
    df['RSI'] = df.loc[:,'RS'].apply(lambda x: 100-(100/(x+1)))
    #BB
    
    df['SMA']= df['Adj Close'].rolling(window = 20).mean()
    #std calculates the standard deviaition
    df['stddev'] = df['Adj Close'].rolling(window=20).std()

    df['Upper'] = df['SMA']+2*df['stddev']
    df['Lower'] = df['SMA']-2*df['stddev']
    df['Buy']= np.where(df.Lower>df.Close,'True','False')
    df['Sell'] = np.where(df.Upper<df.Close,'True','False')
    df.dropna(inplace =True)

    bollingerCONDITIONS =[
        (df.Buy == "True"),
        (df.Sell =='True'),
        (df.Sell == df.Buy)
    ]

    bollingerCATEGORIES= [
        'Below Lower band','Above Upper  Band', 'Inbetween Bollingers Band'    
    ]
    df['Bollinger Band Signal'] = np.select(bollingerCONDITIONS,bollingerCATEGORIES)
    df['']
    


