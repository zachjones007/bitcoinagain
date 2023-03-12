import requests

def get_market_sentiment(symbol, interval='1d', rsi_time_period=14):
    # Get RSI
    url = f'https://api.coingecko.com/api/v3/coins/{symbol}/market_chart?vs_currency=usd&days=30&interval={interval}'
    response = requests.get(url)
    data = response.json()

    closes = [d[1] for d in data['prices']]
    rsi_values = []
    for i in range(rsi_time_period, len(closes)+1):
        delta = np.diff(closes[i-rsi_time_period:i])
        ups = delta.clip(min=0)
        downs = -1*delta.clip(max=0)
        ups_avg = np.mean(ups)
        downs_avg = np.mean(downs)
        rs = ups_avg / downs_avg
        rsi = 100 - (100 / (1 + rs))
        rsi_values.append(rsi)

    rsi_value = rsi_values[-1]

    # Get Trading Volume
    url = f'https://api.coingecko.com/api/v3/coins/{symbol}/market_chart?vs_currency=usd&days=30&interval={interval}'
    response = requests.get(url)
    data = response.json()

    volumes = [d[1] for d in data['total_volumes']]
    volume_score = ((volumes[-1] - min(volumes)) / (max(volumes) - min(volumes))) * 100

    # Determine Market Sentiment
    if rsi_value < 30:
        sentiment = 'Strongly Bullish'
    elif rsi_value < 50:
        sentiment = 'Bullish'
    elif rsi_value < 70:
        sentiment = 'Neutral'
    elif rsi_value < 90:
        sentiment = 'Bearish'
    else:
        sentiment = 'Strongly Bearish'

    print(f'Market Sentiment: {sentiment}, Volume Score: {volume_score:.2f}')
    return sentiment, volume_score
