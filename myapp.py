import streamlit as st
import yfinance as yf
import pandas as pd

st.write("""
#Simple Stock Price App
Shown Below are the Prices of Stocks and Volume of Google
""")

#Define the Ticker Symbol
tickersymbol = 'GOOGL'

tickerData = yf.Ticker(tickersymbol)
#Get the historical data prices for the ticker
tickerDf= tickerData.history(period = '1d' , start = '2005-5-31', end='2020-5-31')
#Open  High  Low Close  Volume  Dividends  Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
