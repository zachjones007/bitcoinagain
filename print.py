import part1
import part2
import part3

def main():
    result = combine()
    print(result)

def combine():
    sentiment = part1.bullishorbearish(-1)
    score = part2.calculate_rsi_score()
    return sentiment + score

if __name__ == "__main__":
    main()
