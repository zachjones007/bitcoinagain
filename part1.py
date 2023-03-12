import requests

def get_rsi(symbol, days):
    url = f"https://api.coingecko.com/api/v3/coins/{symbol}/market_chart?vs_currency=usd&days={days}"
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
    for c in changes[:14]:
        if c > 0:
            ups += c
        else:
            downs -= c
    avg_up = ups / 14
    avg_down = downs / 14
    rs = avg_up / avg_down
    rsi = 100 - (100 / (1 + rs))
    if rsi < 30:
        return rsi, "Bearish"
    elif rsi > 70:
        return rsi, "Bullish"
    else:
        return rsi, "Neutral"

symbol = 'bitcoin'
days = '14'
rsi_value, market_trend = get_rsi(symbol, days)
print(f'RSI value for {symbol} for the last {days} days is {rsi_value:.2f} and the market trend is {market_trend}.') 
