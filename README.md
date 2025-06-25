# Long-Short Trading Strategy Using Python
Most people assume investing means “buy low, sell high.” But markets aren't always rational. Stocks fall. Volatility increases. Even fundamentally strong companies may underperform.

This is where hedge funds apply a smarter approach — long-short strategies that generate profits regardless of overall market direction. This project aims to recreate a simplified version of that concept using Python.

# Objective
To build a fully automated long-short algorithm that:

1. Goes long on underperforming stocks and shorts those that are outperforming abnormally.

2. Is systematic — operates purely on logic and data, not gut feeling.

3. Is market-neutral — aims to perform in both bull and bear markets.

4. Requires no machine learning or complex black-box models.

5. Is transparent and easy to modify.

6. Inspired by the core logic used in hedge funds like Citadel, Two Sigma, and Renaissance.

# Tools & Libraries Used
1. Python: For scripting and automation.

2. yfinance: To fetch historical stock data (Adjusted Close prices).

3. pandas, numpy: For data manipulation and statistical operations.

4. matplotlib, seaborn: For visualizing returns and performance metrics.

   ![image](https://github.com/user-attachments/assets/00cc168b-bbc5-4b95-aaa5-f5e8ae61db4b)


# Step-by-Step Breakdown
1. Data Acquisition
• Used yfinance to download Adjusted Close prices.

• Adjusted prices account for dividends and stock splits, making comparisons more accurate.

• You can modify the ticker list to test with other stocks or ETFs.

![image](https://github.com/user-attachments/assets/7df87801-e778-4e0d-9b71-87e659d5353b)

2. Log Returns Calculation
• Log returns are used instead of simple percentage changes.

• They are additive over time, making compounding and statistics easier.

![image](https://github.com/user-attachments/assets/83e81539-01be-490c-80a5-416d3036f320)


3. Strategy Logic: Mean Reversion
• For each trading day:

• Compute average return across all selected stocks.

• If a stock’s return is above the average → short it.

• If below the average → long it.

• This is a basic mean-reversion strategy, assuming stocks revert to their average performance.

4. Position Sizing and Portfolio Return
• Long/short positions are assigned weights based on the sign and deviation from the mean.

• Strategy returns are calculated by multiplying positions with daily log returns.

![image](https://github.com/user-attachments/assets/c5fde1ab-d477-43c6-966c-2789cbb8492f)


5. Performance Metrics
• Annualized Return:
Tells you the compounded yearly return if the current performance continued consistently. Useful for comparing strategies over different time frames.

![image](https://github.com/user-attachments/assets/28f76e3b-5045-48da-86f1-cba4d9c93868)


6. Sharpe Ratio:

1. Measures return per unit of risk.

2. Higher Sharpe ratio implies better risk-adjusted performance.

3. Calculated using mean and standard deviation of daily returns.

![image](https://github.com/user-attachments/assets/6b61d710-c02d-42a1-b6f5-f722a3592a43)


# Visual Analysis

• These plots help evaluate the behavior and reliability of the strategy.

• Individual Stock Log Returns

• A multi-line plot showing how each stock has moved over time.

• Helps identify volatility and trends.

![image](https://github.com/user-attachments/assets/423bb559-fa17-4117-8cfb-ba28df6eb05b)

# Histogram of Log Returns (All Stocks)

2. Shows the distribution of log returns over time.

3. Bell curve shape indicates normal behavior; fat tails signal higher risk.

![image](https://github.com/user-attachments/assets/82d3da1f-cc44-4b65-a6b9-b3b5d1fdb9ff)


# Portfolio Strategy Returns (Line Plot)

• Captures daily performance of the overall strategy.

• A smoother curve with upward bias is ideal.

![image](https://github.com/user-attachments/assets/82b6a9e5-ed7c-482a-9003-54c576d8a22d)

# Distribution of Strategy Returns (Histogram)

• Evaluates the consistency and spread of profits/losses.

• Narrow, centered curves suggest stable performance.

![image](https://github.com/user-attachments/assets/dfc519ef-7b2f-44a9-8dd1-b4318cec991f)



# Conclusion
This project demonstrates how you can create a basic, transparent, and logic-driven trading algorithm using historical price data and simple statistics.
No machine learning involved.
Easy to understand, modify, and scale.
Works as a solid foundation to build more advanced strategies.

For more depth in this topic, read and subscrible my Substack Bio

Substack Home: https://substack.com/@shauryakohli?utm_source=user-menu

LinkedIn: www.linkedin.com/in/shaurya-kohli18


