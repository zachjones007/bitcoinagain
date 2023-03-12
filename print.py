import os
import sys

# add the bitcoinagain directory to the path
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from bitcoinagain.part1 import get_rsi
from bitcoinagain.part2 import get_market_trend
from bitcoinagain.part3 import get_market_sentiment

def print_results(symbol='BTCUSDT', interval='1d', rsi_time_period=14):
    rsi_value = get_rsi(symbol, interval, rsi_time_period)
    market_trend = get_market_trend(symbol, interval)
    market_sentiment = get_market_sentiment(symbol, interval, rsi_time_period)

    print(f'Part 1 - RSI Values:\n{rsi_value}')
    print(f'Part 2 - Market Trend:\n{market_trend}')
    print(f'Part 3 - Market Sentiment:\n{market_sentiment}')

print_results()

