import yfinance as yf

# Retrieve DXY data from Yahoo Finance
dxy = yf.Ticker("^DXY")
df = dxy.history(period="1d")

# Calculate RSI using the talib library
import talib

rsi = talib.RSI(df["Close"], timeperiod=14)[-1]
print("RSI:", rsi)
