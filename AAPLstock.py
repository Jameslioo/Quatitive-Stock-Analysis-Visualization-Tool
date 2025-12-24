import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# 1. obtaining data: downloading AAPL stock data in the past year.
print("Downloading...")
ticker = "AAPL" 
data = yf.download(ticker, period="1y")

# 2. Quatitive caculation: caculate 20-day SMA.
# Logic: Value for each day = average of closing price in the past 20 days.
data['SMA_20'] = data['Close'].rolling(window=20).mean()

# 3. Visualistion: draw a picture.
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Close'], label='Close Price', alpha=0.5) # Closing price: semi-transparent.
plt.plot(data.index, data['SMA_20'], label='20-Day SMA', color='orange', linewidth=2) # SMA, bolded orange.
plt.title(f"{ticker} Stock Price & 20-Day Moving Average")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True)
plt.show()
