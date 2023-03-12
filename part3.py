import os
import sys
import requests
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
        sentiment = 1
    elif market_trend == 'Bearish':
        sentiment = -1
    else:
        if rsi_value < 30:
            sentiment = 1
        elif rsi_value > 70:
            sentiment = -1
        else:
            sentiment = 0

    return sentiment

symbol = 'bitcoin'
rsi_value = get_rsi(symbol)
market_trend = get_market_trend(symbol)
market_sentiment = get_market_sentiment(symbol)

if market_sentiment == 1:
    print('Market Sentiment: Positive (Bullish)')
elif market_sentiment == -1:
    print('Market Sentiment: Negative (Bearish)')
else:
    print('Market Sentiment: Neutral')

print('RSI Value:', rsi_value)
print('Market Trend:', market_trend)
