import os
from boto.s3.connection import S3Connection
from alpha_vantage.timeseries import TimeSeries
import streamlit as st
import pandas as pd
from datetime import datetime

# API_key = os.environ.get('API_ALPHA_VANTAGE')
API_key = S3Connection(os.environ['API_ALPHA_VANTAGE'])

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
    adjusted_close = df['Adjusted close']
    if len(month) > 0:
        st.line_chart(adjusted_close.loc[month+' '+'2021'])
