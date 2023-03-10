import pandas as pd
import requests
from bs4 import BeautifulSoup

# Define statements as a global variable
statements = []

# Part 1
def fetch_fed_statements():
    global statements
    # ... code to fetch and process statements ...

# Part 2
def market_sentiment_score():
    # ... code to analyze sentiment and calculate accuracy ...

# Part 3
  if __name__ == "__main__":
    # Run part 1
    fed_df = fetch_fed_statements()
    print("Federal Reserve Statements:\n", fed_df.head(), "\n")

    # Run part 2
    acc = market_sentiment_score()
    print("Accuracy:", acc)
