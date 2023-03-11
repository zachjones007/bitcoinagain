import part1
import part2

def calculate_combined_score():
    sentiment = 1 if part1.bullishorbearish() == "Bullish" else -1
    score = part2.calculate_rsi_score()
    return sentiment * score

