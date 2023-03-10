#part 3
from part1 import sentimen
from part2 import get_bitcoin_data, analyze_bitcoin

def main():
    # Get data from APIs
    bitcoin_data = get_bitcoin_data()
    federal_reserve_data = analyze_federal_reserve()

    # Analyze data
    bitcoin_analysis = analyze_bitcoin(bitcoin_data)
    federal_reserve_analysis = analyze_federal_reserve(federal_reserve_data)

    # Determine overall market sentiment
    sentiment = bitcoin_analysis + sentimen
    if sentiment > 0:
        print("Market sentiment is bullish.")
    elif sentiment < 0:
        print("Market sentiment is bearish.")
    else:
        print("Market sentiment is neutral.")

if __name__ == "__main__":
    main()1
