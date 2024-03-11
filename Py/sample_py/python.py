import pandas as pd
import yahooquery as yq
import time
import random

SYMBOL_URL = "https://ja.wikipedia.org/wiki/%E6%9D%B1%E4%BA%AC%E8%A8%BC%E5%88%B8%E5%8F%96%E5%BC%95%E6%89%80%E3%83%97%E3%83%A9%E3%82%A4%E3%83%A0%E5%B8%82%E5%A0%B4%E4%B8%8A%E5%A0%B4%E4%BC%81%E6%A5%AD%E4%B8%80%E8%A6%A7"

def collect_symbol() -> pd.DataFrame:
    df = pd.read_html(SYMBOL_URL)
    return df[0]

def read_historical_data(code:int,name:str):
    time.sleep(random.randint(1,5))
    ticker = yq.Ticker(f'{code}.T')
    save_df_to_csv(ticker.history(period='60d',interval="id"),file_name_name)

def save_df_to_csv(df:pd.DataFrame,file_name:str):
    df.to_csv(path_or_buf=f"../CSVs/{file_name}.csv" ,encoding='cp932')




if __name__ == "__main__":
    symbol_df = collect_symbol()
    for row in symbol_df.loc[:,['コード','銘柄名']].itertuples():
        print (row)
        read_historical_data (row.コード,row.銘柄名)

    print ('Done')