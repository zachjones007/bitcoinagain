import part1
import part2

def combine():
    sentiment = part1.determine_market_trend(-1)
    score = part2.calculate_rsi_score()
    return sentiment + score

def main():
    result = combine()
    print(f"The combined score is: {result}")

if __name__ == "__main__":
    main()
