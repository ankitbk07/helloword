import pandas as pd
import matplotlib.pyplot as plt


def rsiChecker(df):
    RSI_PERIOD = 14   
    #Rsi
    df['Change'] = df['Adj Close'].diff()
    df['Up'] = df['Change'].apply(lambda x: x if x>0 else 0)
    df['Down'] =df['Change'].apply(lambda x:x if x<0 else 0)
    df['avg Up'] = df['Up'].ewm(span = RSI_PERIOD-1).mean()
    df['avg Down'] = df['Down'].ewm(span = RSI_PERIOD-1).mean()
    df = df.dropna()
    df['RS']  = abs(df.loc[:,'avg Up']/df.loc[:,'avg Down'])
    df['RSI'] = df.loc[:,'RS'].apply(lambda x: 100-(100/(x+1)))
    df.to_csv('rsi.csv',index=False)     
    return df.drop(columns = ['Change','Up','Down','avg Up','avg Down','RS'])

     
     

    