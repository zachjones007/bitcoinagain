import part1
import part2

def calculate_combined_score():
    sentiment = part1.get_fed_data()
    score = part2.calculate_rsi_score()
    return sentiment + score
