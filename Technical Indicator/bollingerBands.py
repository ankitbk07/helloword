# import pandas as pd
import  numpy as np 
# import matplotlib.pyplot as plt
# import yfinance as yf

# df = yf.download('MSFT',start= '2021-01-01')
# df.to_csv('MSFT.csv')

def bolingerBandIndicator(df):
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
    return df.drop(columns =['SMA','stddev','Upper','Lower','Buy','Sell'])







