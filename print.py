def print_results():
    symbol = 'BTCUSDT'
    interval = '1d'
    rsi_time_period = 14

    # Part 1 - RSI Values
    rsi_value = get_rsi(symbol, interval, rsi_time_period)
    print('Part 1 - RSI Values:')
    print(rsi_value)

    # Part 2 - Overbought/Oversold Values
    overbought_oversold = get_overbought_oversold(symbol, interval)
    print('Part 2 - Overbought/Oversold Values:')
    if overbought_oversold == "Overbought":
        print("Overbought")
    elif overbought_oversold == "Oversold":
        print("Oversold")
    else:
        print("Neutral")

    # Part 3 - Analysis Result
    market_sentiment = get_market_sentiment(symbol, interval, rsi_time_period)
    print('Part 3 - Analysis Result:')
    print(market_sentiment)
