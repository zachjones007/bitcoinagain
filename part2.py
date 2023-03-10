#part 2


import yfinance as yf
import pandas as pd
from ta.momentum import RSIIndicator

def get_bitcoin_data():
    data = yf.download("BTC-USD", start="2010-01-01", end="2022-01-01")
    # Calculate RSI
    indicator = RSIIndicator(data['Close'], window=14)
    data['RSI'] = indicator.rsi()
    # Drop rows with missing values
    data = data.dropna()
    return data

