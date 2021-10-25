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

import numpy as np
import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import requests
import streamlit as st

class data_n_util:
    def __init__(self, data_fpn='data/test_pred.csv'):
        self.data_fpn = data_fpn
        self.df = self.load_data(data_fpn)
    
    @st.cache
    def load_data(self, data_fpn):
        load_dotenv()
        df = pd.read_csv(data_fpn)
        df['ae_pred_xgbr_untuned'] = df.pred_xgbr_untuned - df.found_helpful_percentage
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
    my_data = data_n_util()

    # make plot!
    # fig = px.scatter(df, x='found_helpful_percentage', y='pred_rfr_untuned', labels={'4. close': 'closing price'})
    # fig.add_shape(type='line',
    #     x0=0, y0=0, x1=1, y1=1,
    #     line=dict(
    #             color='MediumPurple',
    #             width=4,
    #             dash='dot',
    #         )
    # )
    fig_diff = px.histogram(my_data.df, x='ae_pred_xgbr_untuned', labels={
                     'ae_pred_xgbr_untuned': 'prediction - truth'},
                     title='Mean Absolute Error = {:.2f}'.format(np.abs(my_data.df.ae_pred_xgbr_untuned).mean()))
    fig_scat = go.FigureWidget()
    fig_scat.add_scatter(
        x=my_data.df.found_helpful_percentage,
        y=my_data.df.pred_lstm2_untuned,
        mode='markers'
    )
    st.plotly_chart(fig_diff)