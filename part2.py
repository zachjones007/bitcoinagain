#part 2 
import yfinance as yf
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from transformers import BertTokenizer, BertForSequenceClassification
import torch
from pytrends.request import TrendReq

def market_sentiment_score():
    # Fetch historical data for Bitcoin
    btc = yf.Ticker("BTC-USD")
    data = btc.history(period="max")

    # Load the pre-trained BERT model and tokenizer
    model = BertForSequenceClassification.from_pretrained("bert-base-uncased")
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

    # Analyze the sentiment of the statements made by the Federal Reserve
    statements = ["The Federal Reserve is committed to maintaining price stability and supporting the economic recovery.", "The Federal Reserve is concerned about rising inflation and may raise interest rates."]
    scores = []
    for statement in statements:
        input_ids = torch.tensor([tokenizer.encode(statement, add_special_tokens=True)])
        with torch.no_grad():
            output = model(input_ids)[0]
        score = torch.sigmoid(output[0,0]).item()
        scores.append(score)

    # Create a Pytrends object and fetch Google Trends data for Bitcoin
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload(kw_list=['Bitcoin'], timeframe='today 5-y')
    interest_over_time = pytrends.interest_over_time()

    # Add RSI column to the historical data
    delta = data['Close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=12).mean()
    avg_loss = loss.rolling(window=12).mean()
    rs = avg_gain / avg_loss
    data['RSI'] = 100 - (100 / (1 + rs))

    # Add oversold/overbought column
    oversold = (data['RSI'] < 30)
    overbought = (data['RSI'] > 70)
    data['oversold'] = oversold
    data['overbought'] = overbought

    # Assign sentiment scores to the historical data DataFrame
    data['sentiment'] = [scores[i % len(scores)] for i in range(len(data))]

    # Create a new column for the label, 1 for an increase in price and 0 for a decrease
    data['label'] = (data['Close'] > data['Close'].shift(1)).astype(int)

    # Create a feature dataset, dropping unnecessary columns
    features = data[['RSI','sentiment', 'oversold', 'overbought']]

    # Fill missing values with mean and drop rows with missing values
    features = features.fillna(features.mean()).dropna()

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, data['label'], test_size=0.2, random_state=42)

    # Create a logistic regression model
    log_reg = LogisticRegression()

    # Train the model on the training data
    log_reg.fit(X_train, y_train)

    # Test the model on the testing data
    y_pred = log_reg.predict(X_test)

    # Calculate the accuracy of the model
    accuracy = (y_pred == y_test).mean()

    return accuracy
