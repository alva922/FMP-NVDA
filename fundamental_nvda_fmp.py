#Fundamental Analysis of NVDA using Financial Modeling Prep (FMP) API in Python
#https://medium.com/@slisowski/support-your-algorithmic-trading-with-fundamental-data-e81781b10d9d
#https://benjaq.medium.com/a-simple-guide-how-to-use-the-financial-modeling-prep-api-in-python-b3e03e742fb8
#https://pypi.org/project/fmp-python/
#https://github.com/ddalgotrader/support_trading_fundamental_data/blob/main/FmpConnector.py
import os
os.chdir('YOURPATH')    # Set working directory
os. getcwd()
#!pip install fmp-python
from fmp_python.fmp import FMP
fmp = FMP(api_key='your_api_key')
fmp.get_quote('NVDA')
from fmp_api_python.fmp import FMPClient
client = FMPClient('your_client_code')
#Connected
msft_info_df=fmp_api.get_company_info(symbol='NVDA', info_type='company_profile')
print(msft_info_df)
msft_info_df=fmp_api.get_company_info(symbol='NVDA', info_type='company_rating')
print(msft_info_df)
tesla_info_df=fmp_api.get_financial_data(symbol='NVDA', report_type='balance_statement', period='annual', limit=10)
print(tesla_info_df)
tesla_price_df=fmp_api.get_daily_prices(symbol='NVDA')
tesla_price_df.to_csv('nvda_stock_price_2019_2024.csv', sep='\t', encoding='utf-8')
fmp_api.draw_chart(tesla_price_df)
# 
# fig1
