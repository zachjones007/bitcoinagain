import os
import sys
import numpy as np
import pandas as pd

# add the bitcoinagain directory to the path
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

# import the part1 and part2 functions
from bitcoinagain.part1 import get_rsi
from bitcoinagain.part2 import get_overbought_oversold
from bitcoinagain.part3 import get_market_sentiment

symbol = 'BTCUSDT'
interval = '1d'
rsi_time_period = 14
market_sentiment = get_market_sentiment(symbol, interval, rsi_time_period)
print('Market Sentiment:', market_sentiment)
