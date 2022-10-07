import pandas as pd
import vectorbt as vbt

size = pd.Series([1, -1, 1, -1])  # per row
price = pd.DataFrame({'a': [1, 2, 3, 4], 'b': [4, 3, 2, 1]})  # per element
direction = ['longonly', 'shortonly']  # per column
fees = 0.01  # per frame

pf = vbt.Portfolio.from_orders(price, size, direction=direction, fees=fees)
print(pf.orders.records_readable)


entries = pd.Series([True, False, True, False])
exits = pd.Series([False, True, False, True])

pf = vbt.Portfolio.from_signals(price, entries, exits, size=1, direction=direction, fees=fees)
pf.orders.records_readable