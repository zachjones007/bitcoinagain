import requests
import numpy as np
import pandas as pd

def get_rsi(symbol, interval, time_period):
    url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}'
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data)
    df = df.iloc[:,:6]
    df.columns = ['time', 'open', 'high', 'low', 'close', 'volume']
    df = df.astype(float)
    delta = df['close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=time_period).mean()
    avg_loss = loss.rolling(window=time_period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi.iloc[-1]

def get_overbought_oversold(symbol, interval):
    url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}'
    response = requests.get(url)
    data = response.json()
    close_prices = [float(entry[4]) for entry in data]
    high_prices = [float(entry[2]) for entry in data]
    low_prices = [float(entry[3]) for entry in data]
    for i in range(len(close_prices)):
        if high_prices[i] > 0:
            rsi = 100 - (100 / (1 + (close_prices[i] / high_prices[i])))
            break
        elif low_prices[i] > 0:
            rsi = 100 - (100 / (1 + (close_prices[i] / low_prices[i])))
            break
    overbought = (rsi >= 70)
    oversold = (rsi <= 30)
    return overbought, oversold

def get_market_sentiment(symbol, interval='1d', rsi_time_period=14):
    rsi_value = get_rsi(symbol, interval, rsi_time_period)
    overbought, oversold = get_overbought_oversold(symbol, interval)
    if overbought:
        sentiment = 100
    elif oversold:
        sentiment = 0
    else:
        sentiment = (rsi_value - 30) * 100 / 40
    return sentiment

symbol = 'BTCUSDT'
interval = '1d'
rsi_time_period = 14
market_sentiment = get_market_sentiment(symbol, interval, rsi_time_period)
print('Market Sentiment:', market_sentiment)
