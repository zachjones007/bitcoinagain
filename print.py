from part1 import Bitcoin
from part2 import Trade
from part3 import Analysis

def print_results():
    bitcoin = Bitcoin()
    trade = Trade()
    analysis = Analysis()

    data1 = bitcoin.get_historical_data()
    data2 = trade.get_trades()
    result = analysis.analyze()

    # Print out the results
    print("Part 1 - RSI Values:")
    print(data1['rsi'])
    print("Part 2 - Overbought/Oversold Values:")
    print("Overbought:", data2['overbought'])
    print("Oversold:", data2['oversold'])
    print("Part 3 - Analysis Result:")
    print(result)

if __name__ == '__main__':
    print_results()
