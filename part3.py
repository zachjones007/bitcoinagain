# Define statements as a global variable
statements = []

def fetch_fed_statements():
    global statements
    # ... code to fetch and process statements ...


def market_sentiment_score():
    # ... code to analyze sentiment and calculate accuracy ...


  if __name__ == "__main__":
    #df
    fed_df = fetch_fed_statements()
    print("Federal Reserve Statements:\n", fed_df.head(), "\n")

    #acc
    acc = market_sentiment_score()
    print("Accuracy:", acc)
