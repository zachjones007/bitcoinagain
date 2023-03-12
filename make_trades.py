from get_market_data import get_price, get_volume

def make_trade():
    price = get_price()
    volume = get_volume()
    if price < 50000 and volume > 100000000:
        return 'buy'
    elif price > 55000:
        return 'sell'
    else:
        return 'hold'

if __name__ == '__main__':
    print(f"Trade decision: {make_trade()}")
