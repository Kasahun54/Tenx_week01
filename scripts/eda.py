import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('financial_news.csv')

# Perform EDA
print(data.describe())
data['headline_length'].plot.hist()
plt.show()
