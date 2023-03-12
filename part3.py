import os
from binance.client import Client
from make_trades import make_trade

api_key = os.getenv('BINANCE_API_KEY')
api_secret = os.getenv('BINANCE_API_SECRET')
client = Client(api_key, api_secret)

def execute_trade():
    decision = make_trade()
    if decision == 'buy':
        order = client.create_order(
            symbol='BTCUSDT',
            side=Client.SIDE_BUY,
            type=Client.ORDER_TYPE_MARKET,
            quantity=0.001
        )
        print("Bought 0.001 BTC")
    elif decision == 'sell':
        order = client.create_order(
            symbol='BTCUSDT',
            side=Client.SIDE_SELL,
            type=Client.ORDER_TYPE_MARKET,
            quantity=0.001
        )
        print("Sold 0.001 BTC")
    else:
        print("No trade made")

if __name__ == '__main__':
    execute_trade()

