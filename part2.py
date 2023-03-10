#part 2



import requests
import pandas as pd

def get_btc_price_data():
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=90"
    response = requests.get(url)
    if response.ok:
        data = response.json()
        prices = data.get("prices", [])
        df = pd.DataFrame(prices, columns=["timestamp", "price"])
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
        df = df.set_index("timestamp")
        return df
    else:
        return pd.DataFrame()

def market_sentiment_score():
    # Fetch historical price data for Bitcoin
    price_data = get_btc_price_data()

    if not price_data.empty:
        # Calculate the RSI for Bitcoin
        delta = price_data['price'].diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        avg_gain = gain.rolling(window=12).mean()
        avg_loss = loss.rolling(window=12).mean()
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))

        # Return the current sentiment score based on the RSI
        return rsi.iloc[-1]
    else:
        return None
