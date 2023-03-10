#part 3

from part1 import get_bitcoin_price
from part2 import get_bitcoin_data

# Part 1
price = get_bitcoin_price()
print(f"Current Bitcoin price: {price}")

# Part 2
data = get_bitcoin_data()
print(data.head())

# Part 3
print("Part 1 output:")
print(f"Current Bitcoin price: {price}")
print("\nPart 2 output:")
print(data.head())

