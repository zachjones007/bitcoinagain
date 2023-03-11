import requests

def get_bitcoin_prices():
    url = "https://api.coindesk.com/v1/bpi/historical/close.json?start=2022-02-08&end=2022-03-08"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return list(data["bpi"].values())
    else:
        raise Exception(f"Error retrieving prices: {response.status_code} - {response.text}")
        
def determine_market_trend(prices):
    avg_price = sum(prices) / len(prices)
    if prices[-1] > avg_price:
        return 1
    else:
        return -1

if __name__ == "__main__":
    prices = get_bitcoin_prices()
    trend = determine_market_trend(prices)
    print(f"Bitcoin market is {trend} based on the last 30 days of price data.")
