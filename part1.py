#part 1 


import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define function to scrape Federal Reserve statements
def get_fed_statements():
    url = 'https://www.federalreserve.gov/newsevents.htm'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    statements = []
    for link in soup.find_all('a'):
        if 'title' in link.attrs.keys() and 'Press Release' in link.attrs['title']:
            href = link.attrs['href']
            if href.startswith('/newsevents/pressreleases/monetary'):
                date = link.text.strip()
                response = requests.get('https://www.federalreserve.gov'+href)
                soup = BeautifulSoup(response.content, 'html.parser')
                content = soup.find('div', class_='col-xs-12 col-sm-8 col-md-8').get_text().strip()
                statements.append({'date': date, 'content': content})
    return pd.DataFrame(statements)

# Fetch historical data for Bitcoin and Ethereum
btc = yf.Ticker("BTC-USD")
eth = yf.Ticker("ETH-USD")
btc_data = btc.history(period="max")
eth_data = eth.history(period="max")

# Create a function to calculate RSI
def calc_rsi(data, window_length=14):
    delta = data['Close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=window_length).mean()
    avg_loss = loss.rolling(window=window_length).mean()
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

# Calculate RSI for Bitcoin and Ethereum
btc_data['BTC_RSI'] = calc_rsi(btc_data)
eth_data['ETH_RSI'] = calc_rsi(eth_data)

# Merge Bitcoin and Ethereum data into a single DataFrame
data = pd.concat([btc_data['BTC_RSI'], eth_data['ETH_RSI']], axis=1)
data = data.dropna()

# Train a logistic regression model to predict whether to invest in Bitcoin or Ethereum
X_train, X_test, y_train, y_test = train_test_split(data, data.index.get_level_values(0).strftime('%Y-%m-%d'), test_size=0.2, random_state=42)
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)

# Use the model to predict which asset to invest in next
last_date = data.index.get_level_values(0).strftime('%Y-%m-%d')[-1]
last_rsis = data.tail(2).values.flatten()
next_asset = log_reg.predict([last_rsis])[0]

# Print the predicted asset and date
print(f"Next investment on {last_date} should be in {next_asset}")
