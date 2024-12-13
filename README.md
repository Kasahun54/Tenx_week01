# Financial News Sentiment Analysis and Stock Correlation Project

## Project Overview

This project analyzes the correlation between financial news sentiment and stock market movements. It involves:
- **Exploratory Data Analysis (EDA)** to gain insights from news and stock data.
- **Sentiment Analysis** of financial news headlines.
- **Quantitative Analysis** using TA-Lib and PyNance for technical indicators.
- **Correlation Analysis** to study the relationship between sentiment and stock returns.

## Directory Structure

```plaintext
project/
├── .vscode/
│   └── settings.json          # VS Code workspace settings
├── .github/
│   └── workflows/             # GitHub Actions CI/CD
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── src/                       # Core project code
│   ├── __init__.py
│   └── sentiment_analysis.py  # Sentiment analysis code
├── notebooks/                 # Jupyter Notebooks for EDA
│   ├── EDA.ipynb              # Exploratory Data Analysis notebook
│   └── README.md              # Notebook documentation
├── tests/                     # Unit tests
│   ├── __init__.py
│   └── test_sentiment.py      # Test sentiment analysis
└── scripts/                   # Standalone Python scripts
    ├── __init__.py
    ├── eda.py                 # EDA Python script
    └── preprocess.py          # Preprocessing code
