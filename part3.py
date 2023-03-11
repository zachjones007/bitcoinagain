import part1
import part2

def combine():
    sentiment = part1.bullishorbearish(-1)
    score = part2.calculate_rsi_score()
    return sentiment + score
