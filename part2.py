import requests
import numpy as np
import pandas as pd

def get_overbought_oversold(symbol, interval):
    url = f'https://query1.finance.yahoo.com/v7/finance/chart/{symbol}?interval={interval}'
    response = requests.get(url)
    data = response.json()
    timestamps = data['chart']['result'][0]['timestamp']
    close_prices = data['chart']['result'][0]['indicators']['quote'][0]['close']
    high_prices = data['chart']['result'][0]['indicators']['quote'][0]['high']
    low_prices = data['chart']['result'][0]['indicators']['quote'][0]['low']
    for i in range(len(close_prices)):
        if high_prices[i] > 0:
            rsi = 100 - (100 / (1 + (close_prices[i] / high_prices[i])))
            break
        elif low_prices[i] > 0:
            rsi = 100 - (100 / (1 + (close_prices[i] / low_prices[i])))
            break
    if rsi >= 70:
        return "Overbought"
    elif rsi <= 30:
        return "Oversold"
    else:
        return "Neutral"
