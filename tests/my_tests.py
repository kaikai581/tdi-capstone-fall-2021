#!/usr/bin/env python

from datetime import date, datetime
from dotenv import load_dotenv
from time import strptime
import os
import pandas as pd
import requests

def get_all_ticker_symbols(infpn):
    df_sym = pd.read_csv(infpn)
    print(list(df_sym.Symbol))

def vintage_api_request():
    '''
    ref:
    1. https://stackoverflow.com/questions/48071949/how-to-use-the-alpha-vantage-api-directly-from-python
    2. https://medium.com/codex/alpha-vantage-an-introduction-to-a-highly-efficient-free-stock-api-6d17f4481bf
    '''
    load_dotenv()

    API_URL = "https://www.alphavantage.co/query" 
    symbol = 'AMZN'

    data = { "function": "TIME_SERIES_DAILY", 
    "symbol": symbol,
    "outputsize" : "full",
    "datatype": "json",
    "apikey": os.getenv('APIKEY')}

    response = requests.get(API_URL, data)
    response_json = response.json() # maybe redundant

    data = pd.DataFrame.from_dict(response_json['Time Series (Daily)'], orient= 'index').sort_index(axis=1)
    print(data.info()) # check OK or not

if __name__ == '__main__':
    # get_all_ticker_symbols('../data/nasdaq_screener_1624404893542.csv')
    # print([datetime(1900, mint, 1).strftime('%B') for mint in range(1, 13)])
    print(date.today().strftime('%B'))

    # try to request some data
    vintage_api_request()

    # month name to number test
    print(strptime('January','%B').tm_mon)
