import yfinance as yf
import pandas as pd
import numpy as np

def historic_ccy():
    # Define the ticker symbol for USD/MXN
    ticker_symbol = "USDMXN"
    
    # Define the date range for the past month
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=30)
    
    # Fetch the data from Yahoo Finance
    usdmxn_data = yf.download(ticker_symbol, start=start_date, end=end_date)
    
    # Extract the closing prices
    closing_prices = usdmxn_data['Close']
    
    # Print the closing prices for the past month
    print(closing_prices)
