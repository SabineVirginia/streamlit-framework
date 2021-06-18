import os
from alpha_vantage.timeseries import TimeSeries
import streamlit as st

API_key = os.environ.get('API_ALPHA_VANTAGE')

ts = TimeSeries(key=API_key, output_format='pandas')

# Title
st.write("""
# Stock Prices (Monthly)
""")

MSFT_p_ma_data = ts.get_monthly_adjusted('MSFT')
MSFT_p_ma_df = MSFT_p_ma_data[0]
