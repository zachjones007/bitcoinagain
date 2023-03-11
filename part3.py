from part1 import Bitcoin
from part2 import Trade

class Analysis:
    def __init__(self):
        self.bitcoin = Bitcoin()
        self.trade = Trade()

    def analyze(self):
        data1 = self.bitcoin.get_historical_data()
        data2 = self.trade.get_trades()

        rsi = data1['rsi']
        overbought = data2['overbought']
        oversold = data2['oversold']

        # Multiply the RSI value by the number of overbought and oversold levels
        result = rsi * (len(overbought) + len(oversold))

        return result
