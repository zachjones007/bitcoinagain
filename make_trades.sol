//@version=4
strategy(title="Combined Trading Strategy", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=100)

// Moving Average Crossover
ma_short_length = input(title="Short MA Length", type=input.integer, defval=65)
ma_long_length = input(title="Long MA Length", type=input.integer, defval=170)
ma_short = sma(close, ma_short_length)
ma_long = sma(close, ma_long_length)
buy_ma = crossover(ma_short, ma_long)
sell_ma = crossunder(ma_short, ma_long)

// Bollinger Band Breakout
bb_length = input(title="BB Length", type=input.integer, defval=1)
bb_mult = input(title="BB Multiplier", type=input.float, defval=0.1)
[bb_middle, bb_upper, bb_lower] = bb(close, bb_length, bb_mult)
buy_bb = close > bb_upper
sell_bb = close < bb_lower

// RSI Trend Reversal
rsi_length = input(title="RSI Length", type=input.integer, defval=12)
rsi_overbought = input(title="RSI Overbought", type=input.float, defval=69.1)
rsi_oversold = input(title="RSI Oversold", type=input.float, defval=60.667)
rsi = rsi(close, rsi_length)
buy_rsi = rsi < rsi_oversold
sell_rsi = rsi > rsi_overbought

// Buy and Sell Conditions
buy_condition = (buy_ma and buy_bb) or buy_rsi
sell_condition = (sell_ma and sell_bb) or sell_rsi

// Trades
if buy_condition
    strategy.entry("Buy", strategy.long)
    
if sell_condition
    strategy.close("Buy")
    strategy.entry("Sell", strategy.short)

// Plots
plot(ma_short, color=color.blue, title="Short MA")
plot(ma_long, color=color.green, title="Long MA")
plot(bb_middle, color=color.orange, title="Middle BB")
plot(bb_upper, color=color.red, title="Upper BB")
plot(bb_lower, color=color.red, title="Lower BB")
plot(rsi, color=color.purple, title="RSI")

// Debug Info
// plotshape(buy_ma, color=color.green, style=shape.arrowup, location=location.belowbar)
// plotshape(buy_bb, color=color.green, style=shape.triangleup, location=location.belowbar)
// plotshape(buy_rsi, color=color.purple, style=shape.arrowup, location=location.belowbar)
// plotshape(sell_ma, color=color.red, style=shape.arrowdown, location=location.abovebar)
// plotshape(sell_bb, color=color.red, style=shape.triangledown, location=location.abovebar)
// plotshape(sell_rsi, color=color.purple, style=shape.arrowdown, location=location.abovebar)
