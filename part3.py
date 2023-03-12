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

    return sentiment, rsi_value

if __name__ == '__main__':
    symbol = 'bitcoin'
    interval = 'daily'
    rsi_time_period = 14
    market_sentiment, rsi_value = get_market_sentiment(symbol, interval, rsi_time_period)

    if market_sentiment == 1:
        print('Market sentiment is bullish with RSI value of', rsi_value)
    elif market_sentiment == -1:
        print('Market sentiment is bearish with RSI value of', rsi_value)
    else:
        print('Market sentiment is neutral with RSI value of', rsi_value)

