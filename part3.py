# Import necessary libraries and functions from parts 1 and 2
import pandas as pd
from part1 import get_fed_statements
from part2 import market_sentiment_score

# Part 3
if __name__ == "__main__":
    # Run part 1
    fed_df = get_fed_statements()
    print("Federal Reserve Statements:\n", fed_df.head(), "\n")

    # Run part 2
    acc = market_sentiment_score()
    print("Accuracy:", acc)
