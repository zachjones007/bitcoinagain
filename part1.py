import requests

def get_market_sentiment(symbol, interval, rsi_time_period):
    url = f"https://api.coingecko.com/api/v3/coins/{symbol}/market_chart?vs_currency=usd&days=30&interval={interval}"
    response = requests.get(url)
    data = response.json()

    prices = []
    for p in data['prices']:
        prices.append(p[1])

    changes = []
    for i in range(1, len(prices)):
        changes.append(prices[i] - prices[i-1])

    ups = 0
    downs = 0
    for c in changes[:rsi_time_period]:
        if c > 0:
            ups += c
        else:
            downs -= c

    avg_up = ups / rsi_time_period
    avg_down = downs / rsi_time_period
    rs = avg_up / avg_down
    rsi_value = 100 - (100 / (1 + rs))

    if rsi_value < 30:
        sentiment = 'Bearish'
    elif rsi_value > 70:
        sentiment = 'Bullish'
    else:
        sentiment = 'Neutral'

    volume_url = f"https://api.coingecko.com/api/v3/coins/{symbol}"
    volume_response = requests.get(volume_url)
    volume_data = volume_response.json()
    market_data = volume_data['market_data']
    volume_score = market_data['total_volume']['usd'] / market_data['market_cap']['usd']

    return sentiment, volume_score
