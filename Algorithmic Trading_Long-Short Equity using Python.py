# Importing Required Libraries
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Define tickers and date range
stock_names = ['^NYA', 'AAPL', 'TSLA', 'CROX', 'NVDA']
n_years = 10
end_date = datetime.today()
start_date = end_date - timedelta(days=n_years * 365)

# Download the data
stock_data = yf.download(
    tickers=stock_names,
    start=start_date,
    end=end_date,
    auto_adjust=False
)

# Filter only 'Adj Close' prices from MultiIndex
adj_close_cols = [col for col in stock_data.columns if col[0] == 'Adj Close']
adj_close = stock_data[adj_close_cols].copy()

# Rename to just ticker names
adj_close.columns = [col[1] for col in adj_close.columns]

# Daily returns
stock_log_returns = np.log(adj_close / adj_close.shift(1))
average_log_returns = stock_log_returns.mean(axis=1)

# Plot returns
stock_log_returns.plot(figsize=(10, 5))
plt.title("Log Daily Returns")
plt.xlabel("Date")
plt.ylabel("Log Return")
plt.grid(True)
plt.show()

average_log_returns.plot.hist(bins=100)
plt.title("Histogram of Average Log Returns")
plt.xlabel("Return")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# Calculate strategy weights
weights = stock_log_returns.sub(average_log_returns, axis=0) * -1.0
absolute_weights = weights.abs()
absolute_weights_sum = absolute_weights.sum(axis=1)
adjusted_weights = weights.div(absolute_weights_sum, axis=0).dropna()

# Calculate daily strategy returns
ptf_daily_returns = (adjusted_weights.shift(1) * stock_log_returns).dropna()
ptf_daily_returns.plot(figsize=(10, 5))
plt.title("Portfolio Daily Returns")
plt.grid(True)
plt.show()

daily_strategy_returns = ptf_daily_returns.sum(axis=1)
daily_strategy_returns.plot.hist(bins=100)
plt.title("Strategy Daily Returns Distribution")
plt.grid(True)
plt.show()

# Annualized average return
ann_avg_return = 252 * daily_strategy_returns.mean()
print("Annualized Average Return:", ann_avg_return)

# Sharpe Ratio
strategy_mean = daily_strategy_returns.mean()
strategy_std = daily_strategy_returns.std()
sharpe_ratio = np.sqrt(252) * strategy_mean / strategy_std
print("Sharpe Ratio:", sharpe_ratio)
