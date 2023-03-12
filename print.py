import os
import sys

# add the bitcoinagain directory to the path
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

# import the part3 function
from bitcoinagain.part3 import get_market_sentiment

symbol = 'BTCUSDT'
interval = '1d'
rsi_time_period = 14

market_sentiment = get_market_sentiment(symbol, interval, rsi_time_period)

if market_sentiment < 30:
    print('Market Sentiment: 0 (Bearish)')
elif market_sentiment > 70:
    print('Market Sentiment: 100 (Bullish)')
else:
    print(f'Market Sentiment: {market_sentiment:.2f}')

