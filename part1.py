import yfinance as yf
import numpy as np

# Get historical data of US 10-year Treasury yield
data = yf.download("^TNX", period="1y")["Close"]

# Calculate RSI
delta = np.diff(data)
gain = delta * (delta > 0)
loss = -delta * (delta < 0)
avg_gain = np.zeros_like(data)
avg_loss = np.zeros_like(data)
avg_gain[14] = np.mean(gain[:14])
avg_loss[14] = np.mean(loss[:14])
for i in range(15, len(data)):
    avg_gain[i] = (avg_gain[i-1] * 13 + gain[i-1]) / 14
    avg_loss[i] = (avg_loss[i-1] * 13 + loss[i-1]) / 14
rs = avg_gain / avg_loss
rsi = 100 - (100 / (1 + rs))

# Print out the last RSI value
print(f"Last RSI value: {rsi[-1]:.2f}")
