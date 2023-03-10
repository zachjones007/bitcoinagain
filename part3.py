#part 3



import part1
import part2

def combine():
    sentiment, bias = part1.analyze_data()
    score = part2.calculate_rsi()
    combined_score = sentiment + score
    return combined_score, bias
