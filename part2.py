#part 2
import requests
import numpy as np

ENDPOINT = "https://api.pro.coinbase.com"
PRODUCT_ID = "BTC-USD"

def get_price():
    url = f"{ENDPOINT}/products/{PRODUCT_ID}/ticker"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        price = float(data["price"])
        return price
    else:
        raise Exception(f"Error retrieving price: {response.status_code} - {response.text}")

def calculate_rsi(prices, period=14):
    changes = np.diff(prices)
    gains = changes.clip(min=0)
    losses = -changes.clip(max=0)
    avg_gain = np.mean(gains[-period:])
    avg_loss = np.mean(losses[-period:])
    if avg_loss == 0:
        rsi = 100
    else:
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
    return rsi

def main():
    prices = []
    for i in range(15):
        price = get_price()
        prices.append(price)
        print(f"BTC-USD Price: ${price:.2f}")
    rsi = calculate_rsi(prices)
    if np.isnan(rsi):
        print("BTC-USD RSI: N/A")
    else:
        print(f"BTC-USD RSI: {rsi:.2f}")

if __name__ == "__main__":
    main()
