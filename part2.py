#part 2

import yfinance as yf
import pandas as pd

# Fetch historical data for Bitcoin
btc = yf.Ticker("BTC-USD")
data = btc.history(period="max")

# Calculate RSI
delta = data['Close'].diff()
gain = delta.where(delta > 0, 0)
loss = -delta.where(delta < 0, 0)
avg_gain = gain.rolling(window=14).mean()
avg_loss = loss.rolling(window=14).mean()
rs = avg_gain / avg_loss
rsi = 100 - (100 / (1 + rs))

# Calculate the most recent RSI value
recent_rsi = rsi.iloc[-1]

# Scale RSI to -50 to 50 range
scaled_rsi = ((recent_rsi - 50) / 50) * 100

# Print the scaled RSI value
print("Scaled RSI: ", scaled_rsi)
