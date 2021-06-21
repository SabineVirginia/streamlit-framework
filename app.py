import os
from boto.s3.connection import S3Connection
from alpha_vantage.timeseries import TimeSeries
import streamlit as st
import pandas as pd
from datetime import datetime
import altair as alt

API_key = os.environ.get('API_ALPHA_VANTAGE')
# API_key = S3Connection(os.environ['API_ALPHA_VANTAGE'])

ts = TimeSeries(key=API_key, output_format='pandas')

# Title
# Alternative way: st.title('Stock Prices (Monthly)')
st.write("""
# Stock Prices
""")

stock = st.text_input('Enter a ticker:')
month = st.selectbox('Select one of the last five months:', ['February', 'March', 'April', 'May', 'June'])

if len(stock) > 0:
    data = ts.get_daily_adjusted(stock)
    df = data[0]
    df.columns = ['Open', 'High', 'Low', 'Close', 'Adjusted close', 'Volume', 'Dividend amount', 'Split coefficient']
    if len(month) > 0:
        select_df = df.loc[month+' '+'2021']
        select_df = select_df.reset_index()
        # Use Altair because streamlit does not work with my bokeh version at the moment
        price_chart = alt.Chart(select_df).mark_line().transform_fold(['Close', 'Adjusted close'],as_=[' ', 'Price']).encode(alt.X('date:T',
                                                                                                   scale=alt.Scale(zero=False),
                                                                                                   axis=alt.Axis(title='Date')),
                                                                                                   alt.Y('Price:Q',scale=alt.Scale(zero=False),
                                                                                                   axis=alt.Axis(title='Price')),
                                                                                                   color=' :N')
        st.altair_chart(price_chart, use_container_width=True)
