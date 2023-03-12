import os
import sys
import numpy as np
import pandas as pd

# add the bitcoinagain directory to the path
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

# import the part1 and part2 functions
from bitcoinagain.part1 import get_rsi
from bitcoinagain.part2 import get_market_trend

def get_market_sentiment(symbol, interval='1d', rsi_time_period=14):
    rsi_value = get_rsi(symbol, interval, rsi_time_period)
    market_trend = get_market_trend(symbol, interval)
    if market_trend == 'Bullish':
        market_trend_value = 1
    elif market_trend == 'Bearish':
        market_trend_value = -1
    else:
        market_trend_value = 0
        
    # calculate the 20-day moving average
    df = pd.read_csv(f"{symbol}_{interval}.csv")
    df['SMA_20'] = df['Close'].rolling(window=20).mean()
    latest_close = df.iloc[-1]['Close']
    latest_sma = df.iloc[-1]['SMA_20']
    if latest_close > latest_sma:
        sma_trend_value = 1
    else:
        sma_trend_value = -1

    # calculate the market sentiment score as the sum of RSI and trend values
    market_sentiment = rsi_value + market_trend_value + sma_trend_value

    return market_sentiment

