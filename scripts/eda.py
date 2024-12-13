import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
import talib


# Load data
data = pd.read_csv('financial_news.csv')

# Summary statistics
print(data.describe())

# Plot headline length
data['headline_length'] = data['headline'].str.len()
sns.histplot(data['headline_length'])
plt.show()

stock_data = pd.read_csv('stock_prices.csv')

# Calculate moving averages
stock_data['SMA_50'] = talib.SMA(stock_data['Close'], timeperiod=50)
stock_data['RSI'] = talib.RSI(stock_data['Close'])


plt.plot(stock_data['Close'], label='Close Price')
plt.plot(stock_data['SMA_50'], label='50-Day SMA')
plt.legend()
plt.show()
