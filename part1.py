import os
import sys
import numpy as np
import pandas as pd

def get_rsi(symbol, interval='1d', time_period=14):
    api_key = os.environ.get('ALPHAVANTAGE_API_KEY')
    if api_key is None:
        print('API key for Alpha Vantage not found.')
        return None

    url = 'https://www.alphavantage.co/query'
    params = {
        'function': 'RSI',
        'symbol': symbol,
        'interval': interval,
        'time_period': time_period,
        'series_type': 'close',
        'apikey': api_key
    }

    response = requests.get(url, params=params)
    data = response.json()
    if 'Technical Analysis: RSI' not in data:
        print('Error: data not found')
        return None

    rsi_values = []
    for date in sorted(data['Technical Analysis: RSI']):
        rsi_values.append(float(data['Technical Analysis: RSI'][date]['RSI']))

    return rsi_values[-1]

def get_market_trend(symbol, interval='1d'):
    api_key = os.environ.get('ALPHAVANTAGE_API_KEY')
    if api_key is None:
        print('API key for Alpha Vantage not found.')
        return None

    url = 'https://www.alphavantage.co/query'
    params = {
        'function': 'SMA',
        'symbol': symbol,
        'interval': interval,
        'time_period': '50',
        'series_type': 'close',
        'apikey': api_key
    }

    response = requests.get(url, params=params)
    data = response.json()
    if 'Technical Analysis: SMA' not in data:
        print('Error: data not found')
        return None

    sma_values = []
    for date in sorted(data['Technical Analysis: SMA']):
        sma_values.append(float(data['Technical Analysis: SMA'][date]['SMA']))

    if sma_values[-1] > sma_values[-2]:
        return 'Bullish'
    else:
        return 'Bearish'

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

symbol = 'BTCUSDT'
interval = '1d'
rsi_time_period = 14
market_sentiment = get_market_sentiment(symbol, interval, rsi_time_period)
print('Market Sentiment:', market_sentiment)


