import pandas as pd
import vectorbt as vbt
import matplotlib.pyplot as plt
from strategy import Strategy

df = pd.read_csv('project\BTCUSDT-30Minute-Trade.txt')
df['Datetime'] = pd.to_datetime(df['Datetime'])
df.set_index('Datetime', inplace=True)


# strategy==================
@Strategy()
def sma_strategy(df):
    close = df['Close']

    n1 = 200
    n2 = 600

    sma1 = close.rolling(int(n1)).mean()
    sma2 = close.rolling(int(n2)).mean()

    entries = (sma1 > sma2) & (sma1.shift() < sma2.shift())
    exits = (sma1 < sma2) & (sma1.shift() > sma2.shift())
    return entries, exits

sma_strategy.backtest(df, plot=True)
# Portfolio = vbt.Portfolio.from_signals(close, entries, exits, size=1)
# orders = Portfolio.orders

# print(orders.buy.count())
# print(orders.sell.count())
# print(orders.stats())
# print(Portfolio.annual_returns())


# Portfolio.drawdown().plot()
# Portfolio.cumulative_returns().plot()


# print(Portfolio.positions())
# plt.show()
