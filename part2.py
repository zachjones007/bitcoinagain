import requests
import numpy as np
import pandas as pd
from ta.trend import MACD

def get_macd(symbol, interval):
    url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}'
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data)
    df = df.iloc[:,:6]
    df.columns = ['time', 'open', 'high', 'low', 'close', 'volume']
    df = df.astype(float)
    macd = MACD(df['close']).macd()
    signal = MACD(df['close']).macd_signal()
    return macd.iloc[-1], signal.iloc[-1]

def get_market_sentiment(symbol, interval='1d'):
    macd_value, signal_value = get_macd(symbol, interval)
    if macd_value > signal_value:
        sentiment = 100
    elif macd_value < signal_value:
        sentiment = 0
    else:
        sentiment = 50
    return sentiment

symbol = 'BTCUSDT'
interval = '1d'
market_sentiment = get_market_sentiment(symbol, interval)
print('Market Sentiment:', market_sentiment)
