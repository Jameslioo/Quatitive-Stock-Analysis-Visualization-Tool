# Quantitative Stock Analysis & Visualization Tool

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/Library-Pandas-150458)
![Finance](https://img.shields.io/badge/Domain-Quantitative%20Finance-green)

## 📖 Overview

This project is a lightweight quantitative analysis tool designed to automate the retrieval and visualization of historical stock market data.

It utilizes the **Yahoo Finance API** to fetch time-series data and performs technical analysis by calculating the **Simple Moving Average (SMA)**. The tool is designed to help visualize market trends, volatility, and potential crossover signals for large-cap equities (e.g., AAPL, NVDA).

## 🚀 Key Features

* **Automated Data Retrieval:** Fetches real-time and historical OHLCV (Open, High, Low, Close, Volume) data using `yfinance`.
* **Technical Indicator Calculation:** Computes the **20-Day Simple Moving Average (SMA)** to smooth out price noise and identify short-term trends.
* **Data Visualization:** Generates professional-grade financial charts using `Matplotlib`, overlaying price action with moving averages for clear trend analysis.
* **Scalability:** The script is modular and can be easily adapted to analyze any ticker symbol listed on major exchanges.

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Data Manipulation:** Pandas, NumPy
* **Data Source:** yfinance API
* **Visualization:** Matplotlib

## 📊 Example Output

*Below is an example analysis generated for **Apple Inc. (AAPL)**, showing the price action relative to its 20-day moving average over a 1-year period.*

![Stock Analysis Chart](analysis_result.png)
*(Note: Please upload your generated chart image to the repository and name it 'analysis_result.png')*

## 💻 How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourUsername/stock-market-analysis.git](https://github.com/YourUsername/stock-market-analysis.git)
    cd stock-market-analysis
    ```

2.  **Install dependencies:**
    ```bash
    pip install pandas yfinance matplotlib
    ```

3.  **Run the script:**
    ```bash
    python analysis.py
    ```

## 🔮 Future Improvements (Roadmap)

To further enhance the analytical capabilities, the following features are planned:

* **Advanced Indicators:** Implementation of RSI (Relative Strength Index) and MACD for momentum analysis.
* **Backtesting Engine:** A simple framework to simulate trading strategies based on SMA crossovers.
* **Risk Metrics:** Calculation of annualized volatility and Sharpe Ratio.

## 👤 Author

**James Liu**
* **University:** The Hong Kong University of Science and Technology (HKUST)
* **Major:** Computer Science (CSE)
* **Contact:** yliuqz@connect.ust.hk
* **LinkedIn:** https://www.linkedin.com/in/james-liu-abba33398/
