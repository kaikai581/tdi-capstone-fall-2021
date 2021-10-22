#!/usr/bin/env python
'''
My data dashboard for stock ticker with Streamlit.
Source reference:
https://github.com/jkanner/streamlit-dataview/blob/master/app.py
with the website:
https://share.streamlit.io/jkanner/streamlit-dataview/master/app.py/+/
'''

from datetime import date, datetime
from dotenv import load_dotenv
from time import strptime
import os
import pandas as pd
import plotly.express as px
import requests
import streamlit as st

@st.cache
def get_data(selected_stock):
    load_dotenv()
    API_URL = 'https://www.alphavantage.co/query'
    symbol = selected_stock

    data = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': symbol,
    'outputsize': 'full',
    'datatype': 'json',
    'apikey': os.getenv('APIKEY')}

    response = requests.get(API_URL, data)
    response_json = response.json() # maybe redundant

    df = pd.DataFrame.from_dict(response_json['Time Series (Daily)'], orient= 'index').sort_index(axis=1)
    df = df.apply(pd.to_numeric)
    df['date'] = pd.to_datetime(df.index)
    # df['date'] = pd.to_datetime(df['date'].dt.date)
    return df

if __name__ == '__main__':
    #
    # render the main window
    #
    st.set_page_config(page_title='Shih-Kai\'s Capstone Project')
    # Title the app
    st.title('Predicting Usefulness of Written Reviews')

    # st.markdown('''
    # ## Shih-Kai Lin's Milestone Project
    # * Use the menu at left to select data
    # * Your plots will appear below
    # ''')

    #
    # render the side control bar
    #
    st.sidebar.markdown('# Select plot parameters:')
    df_sym = pd.read_csv('data/nasdaq_screener_1624404893542.csv')
    stock_list = list(df_sym.Symbol)
    selected_stock = st.sidebar.selectbox('Ticker (e.g. AAPL):',
                                            stock_list,
                                            index=stock_list.index('AMZN'))
    
    # select year
    selected_year = st.sidebar.selectbox('Year:',
                                            list(reversed(range(2010, date.today().year+1))))
    
    # select month
    month_list = [datetime(1900, mint, 1).strftime('%B') for mint in range(1, 13)]
    selected_month = st.sidebar.selectbox('Month:',
                                            month_list,
                                            index=month_list.index(date.today().strftime('%B')))
    
    # retrieve data with Alpha Vantage API
    df = get_data(selected_stock)
    df_selected = df[(df.date.dt.month == strptime(selected_month,'%B').tm_mon)
                     & (df.date.dt.year == selected_year)]

    # show the retrieved data in a table
    # st.table(df_selected)

    # make plot!
    fig = px.line(df_selected, x='date', y='4. close', labels={'4. close': f'{selected_stock} closing price'})
    st.plotly_chart(fig)