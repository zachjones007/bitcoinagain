import requests
import numpy as np

class Trade:
    def __init__(self):
        self.base_url = 'https://api.pro.coinbase.com'
        self.product_id = 'BTC-USD'

    def get_trades(self):
        url = f"{self.base_url}/products/{self.product_id}/candles"
        params = {
            'granularity': '86400' # 1 day
        }
        response = requests.get(url, params=params)

        data = response.json()
        prices = [float(row[4]) for row in data]
        rsi = self.calculate_rsi(prices)
        overbought, oversold = self.calculate_overbought_oversold(rsi)

        return {
            'overbought': overbought,
            'oversold': oversold
        }

    def calculate_rsi(self, data, period=14):
        # Calculate the gains and losses for each period
        changes = [data[i] - data[i-1] for i in range(1, len(data))]
        gains = [max(0, x) for x in changes]
        losses = [max(0, -x) for x in changes]

        # Calculate the average gains and losses over the specified period
        avg_gain = sum(gains[:period]) / period
        avg_loss = sum(losses[:period]) / period

        # Calculate the initial RSI value
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))

        # Calculate the RSI values for subsequent periods
        for i in range(period, len(data)):
            change = data[i] - data[i-1]
            gain = max(0, change)
            loss = max(0, -change)

            avg_gain = ((period - 1) * avg_gain + gain) / period
            avg_loss = ((period - 1) * avg_loss + loss) / period

            rs = avg_gain / avg_loss
            rsi = 100 - (100 / (1 + rs))

        return rsi

    def calculate_overbought_oversold(self, rsi, overbought_threshold=70, oversold_threshold=30):
        overbought = np.argwhere(rsi >= overbought_threshold).flatten()
        oversold = np.argwhere(rsi <= oversold_threshold).flatten()

        return overbought, oversold
