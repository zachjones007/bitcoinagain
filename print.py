from bitcoinagain.part1 import get_rsi
from bitcoinagain.part2 import get_market_trend
from bitcoinagain.part3 import get_market_sentiment

def print_results():
    symbol = 'BTCUSDT'
    interval = '1d'
    rsi_time_period = 14

    # get RSI from part 1
    rsi = get_rsi(symbol, interval, rsi_time_period)
    print(f'RSI: {rsi}')

    # get market trend from part 2
    market_trend = get_market_trend(symbol, interval)
    print(f'Market Trend: {market_trend}')

    # get market sentiment from part 3
    market_sentiment = get_market_sentiment(symbol, interval, rsi_time_period)
    print(f'Market Sentiment: {market_sentiment}')

print_results()
