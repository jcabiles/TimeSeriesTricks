import pandas as pd
from datetime import datetime

stocks = pd.read_csv('stocks.csv', index_col=0)
bonds = pd.read_csv('bonds.csv', index_col=0)
