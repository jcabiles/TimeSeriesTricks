import pandas as pd
import matplotlib.pyplot as plt

# row 1 is useless so we can skip it to get the correct headers
# let's also make sure that 'Week' is used as the index
diet = pd.read_csv("diet_google_trends.csv", skiprows=1, index_col=0)
diet.index = pd.to_datetime(diet.index)

# plot
diet.plot(grid=True)
plt.show()

# slice by particular year
diet2015 = diet['2015']
diet2015.plot(grid=True)
plt.show()