# Import necessary libraries
import pandas as pd
from pytrends.request import TrendReq

# Define function to get Google Trends data
def get_google_trends_data(keyword, timeframe='today 5-y', geo='US'):
    pytrends = TrendReq()
    pytrends.build_payload([keyword], cat=0, timeframe=timeframe, geo=geo, gprop='')
    data = pytrends.interest_over_time()[[keyword]]
    data.drop(labels=['isPartial'], axis=1, inplace=True)
    return data

# Define function to preprocess the data
def preprocess_data(data):
    # Drop rows with missing values
    data = data.dropna()
    # Normalize the data
    data = (data - data.mean()) / data.std()
    # Add a column of 1s to serve as the intercept term
    data['intercept'] = 1
    # Rearrange columns so that intercept column is first
    cols = data.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    data = data[cols]
    return data

# Define function to perform linear regression
def linear_regression(data):
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]
    beta = pd.Series([0] * X.shape[1])
    while True:
        residuals = y - X.dot(beta)
        gradient = -2 * X.T.dot(residuals)
        if gradient.abs().max() < 0.0001:
            break
        else:
            beta = beta - 0.00001 * gradient
    return beta

# Get Google Trends data for Bitcoin
data = get_google_trends_data('Bitcoin')

# Preprocess the data
data = preprocess_data(data)

# Perform linear regression on the preprocessed data
beta = linear_regression(data)

# Print the coefficients
print("The coefficients are: ")
print(beta)

