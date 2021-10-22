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
def get_data():
    load_dotenv()
    df = pd.read_csv('data/test_pred.csv')
    
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
    # df_sym = pd.read_csv('data/nasdaq_screener_1624404893542.csv')
    # stock_list = list(df_sym.Symbol)
    # selected_stock = st.sidebar.selectbox('Ticker (e.g. AAPL):',
    #                                         stock_list,
    #                                         index=stock_list.index('AMZN'))

    # show the retrieved data in a table
    # st.table(df_selected)
    df = get_data()

    # make plot!
    fig = px.scatter(df, x='found_helpful_percentage', y='pred_rfr_untuned', labels={'4. close': 'closing price'})
    fig.add_shape(type='line',
        x0=0, y0=0, x1=1, y1=1,
        line=dict(
                color='MediumPurple',
                width=4,
                dash='dot',
            )
    )   
    st.plotly_chart(fig)