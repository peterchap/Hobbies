import pandas as pd
import streamlit as st
import yfinance as yf
import cufflinks as cf
import datetime
from pytickersymbols import PyTickerSymbols
from pandas_datareader import data as pdr

yf.pdr_override()
stock_data = PyTickerSymbols()
countries = stock_data.get_all_countries()
indices = stock_data.get_all_indices()
industries = stock_data.get_all_industries()

uk_stocks = stock_data.get_stocks_by_index('FTSE 100')

print(list(uk_stocks))

st.set_page_config(layout="wide")

st.set_page_config(layout="wide")

# App Title
st.markdown("Stock Portfolio Performance App")

# Sidebar

st.sidebar()
