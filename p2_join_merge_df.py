import pandas as pd

stocks = pd.read_csv('stocks.csv', index_col=0)
bonds = pd.read_csv('bonds.csv', index_col=0)