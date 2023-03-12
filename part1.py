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

symbol = 'BTCUSDT'
interval = '1d'
time_period = 14
rsi_value = get_rsi(symbol, interval, time_period)
print('RSI:', rsi_value)
