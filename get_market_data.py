import requests

def get_price():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    return data['bitcoin']['usd']

def get_volume():
    url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=1'
    response = requests.get(url)
    data = response.json()
    volume = 0
    for d in data['total_volumes']:
        volume += d[1]
    return volume

if __name__ == '__main__':
    print(f"Bitcoin price: {get_price()}")
    print(f"Bitcoin volume: {get_volume()}")
