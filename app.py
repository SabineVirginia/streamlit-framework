import os
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.fundamentaldata import FundamentalData

API_key = os.environ.get('API_ALPHA_VANTAGE')

ts = TimeSeries(key=API_key, output_format='pandas')
fd = FundamentalData(key=API_key, output_format='pandas')

MSFT_p_ma_data = ts.get_monthly_adjusted('MSFT')
MSFT_p_ma_df = MSFT_p_ma_data[0]

MSFT_o_data = fd.get_income_statement_annual('MFST')
MSFT_o_df = MSFT_o_data[0]
print(MSFT_o_df)
