import requests
import pandas as pd
import numpy as np

def get_overbought_oversold():
    url = 'https://min-api.cryptocompare.com/data/v2/histoday'
    params = {
        'fsym': 'BTC',
        'tsym': 'USD',
        'limit': '100',
    }

    response = requests.get(url, params=params)
    data = response.json()['Data']['Data']

    df = pd.DataFrame(data)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df.set_index('time', inplace=True)
    df = df.iloc[::-1]

    periods = [14, 30]

    for period in periods:
        delta = df['close'].diff()
        gains, losses = delta.copy(), delta.copy()
        gains[gains < 0] = 0
        losses[losses > 0] = 0

        avg_gain = gains.rolling(window=period).mean()
        avg_loss = losses.abs().rolling(window=period).mean()

        relative_strength = avg_gain / avg_loss
        rsi = 100.0 - (100.0 / (1.0 + relative_strength))

        current_rsi = rsi[-1]

        if current_rsi >= 70:
            return 70
        elif current_rsi <= 30:
            return 30

    return 0
