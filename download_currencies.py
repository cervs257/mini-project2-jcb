import pandas as pd
import yfinance as yf


def download_monthly_prices(tickers):
    data = yf.download(tickers, interval="1m")
    data.to_csv("currency_prices.csv")
