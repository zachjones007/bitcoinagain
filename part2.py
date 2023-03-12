import requests
import numpy as np

def get_ma20(symbol):
    url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval=1d&limit=20'
    response = requests.get(url)
    data = response.json()

    closes = np.array([float(d[4]) for d in data])
    ma20 = np.mean(closes)

    return ma20

def get_market_direction(symbol):
    url = f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}'
    response = requests.get(url)
    data = response.json()

    current_price = float(data['price'])
    ma20 = get_ma20(symbol)

    if current_price > ma20:
        return 1 # bullish
    else:
        return -1 # bearish
