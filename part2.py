import requests
import pandas as pd
import ta

# Set up the API URL and request parameters
url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
params = {"vs_currency": "usd", "days": "1"}

# Make the API request and convert the response to a Pandas DataFrame
response = requests.get(url, params=params).json()
df = pd.DataFrame(response["prices"], columns=["timestamp", "price"])

# Convert the timestamp to a datetime object and set it as the index
df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
df.set_index("timestamp", inplace=True)

# Calculate the RSI using the `ta` library
rsi = ta.momentum.RSIIndicator(df["price"], window=14)
df["rsi"] = rsi.rsi()

# Calculate the overbought/oversold values using the RSI
overbought = 70
oversold = 30
df["overbought"] = overbought
df["oversold"] = oversold

# Determine if the price is overbought or oversold
df["is_overbought"] = df["rsi"] >= overbought
df["is_oversold"] = df["rsi"] <= oversold

# Save the results to a CSV file
df.to_csv("overbought_oversold.csv", index=True)

print("Overbought/Oversold values saved to overbought_oversold.csv")
