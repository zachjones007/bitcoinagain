#part 2


# Import necessary packages and modules
from transformers import BertTokenizer, BertForSequenceClassification
import torch
import pandas as pd
from ta.momentum import RSIIndicator

# Load the pre-trained BERT model and tokenizer
model = BertForSequenceClassification.from_pretrained("bert-base-uncased")
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

def analyze_sentiment(statements):
    # Analyze the sentiment of the statements using BERT
    scores = []
    for statement in statements:
        input_ids = torch.tensor([tokenizer.encode(statement, add_special_tokens=True)])
        with torch.no_grad():
            output = model(input_ids)[0]
        score = torch.sigmoid(output[0,0]).item()
        scores.append(score)
    return scores

def calculate_rsi(data):
    # Add RSI column
    close = pd.DataFrame(data)['close']
    rsi_indicator = RSIIndicator(close, window=14)
    rsi = rsi_indicator.rsi()
    return rsi
