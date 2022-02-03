
import pandas as pd
import rsi,MACD
import bollingerBands as bb 

symbols = ['A','AA','AAC','AAN','AAP','AAPL','AAT','ABM','GOOG','MSFT','TSLA','TWTR']

def technicalIndicatorCalc():
    for symbol in symbols:
        df = pd.read_csv(f"data/{symbol}.csv")
        df1= rsi.rsiChecker(df)
        df2 = MACD.macdIndictor(df1)
        df3 = bb.bolingerBandIndicator(df2)
        df3.to_csv(f'finalData/{symbol}.csv',index =False)
    
if '__main__' == __name__:
    technicalIndicatorCalc()


# df.join(df1)
# df3 = bollingerBands.bolingerBandIndicator(df).to_frame()
# print(type(df2))
# print(type(df3))
# dfs = [df,df1, df2, df3]
# df_final = reduce(lambda left,right: pd.merge(left,right), dfs)
# dfs = [df1, df2, df3]
# dfs = [df.set_index() for df in dfs]
# df_final=dfs[0].join(dfs[1:])
# df_final.to_csv('A_modified.csv')




