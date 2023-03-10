#part 2


import yfinance as yf
import pandas as pd
import numpy as np

def get_bitcoin_data():
    """
    Fetches historical data for Bitcoin from Yahoo Finance and returns it as a pandas DataFrame.
    """
    # Create a Ticker object for Bitcoin
    btc = yf.Ticker("BTC-USD")

    # Fetch historical data
    data = btc.history(period="max")

    return data

def calculate_rsi(data):
    """
    Calculates the Relative Strength Index (RSI) for the given Bitcoin data and returns it as a pandas DataFrame.
    """
    delta = data['Close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=12).mean()
    avg_loss = loss.rolling(window=12).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi.to_frame()

def calculate_label(data):
    """
    Calculates the label (0 or 1) for each row in the given Bitcoin data and returns it as a pandas DataFrame.
    """
    label = (data['Close'] > data['Close'].shift(1)).astype(int)
    return label.to_frame()
