#part 3




from part1 import get_fed_statements
from part2 import get_bitcoin_data

# Fetch the Federal Reserve statements and print them out
statements = get_fed_statements()
print("Federal Reserve Statements:\n", statements, "\n")

# Fetch Bitcoin data and print it out
bitcoin_data = get_bitcoin_data()
print("Bitcoin Data:\n", bitcoin_data.head(), "\n")
