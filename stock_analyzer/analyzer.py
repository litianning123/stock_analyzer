"""
Core functionality for stock analysis
"""


import yfinance as yf
import pandas as pd
import numpy as np
from typing import List, Dict, Tuple


def calculate_rsi(data: pd.Series, period: int = 14) -> float:
   """
   Calculate RSI for a given price series
   """
   delta = data.diff()
   gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
   loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
   rs = gain / loss
   return 100 - (100 / (1 + rs)).iloc[-1]


def calculate_bollinger_bands(data: pd.Series, period: int = 20, std_dev: float = 2) -> Tuple[float, float, float]:
   """
   Calculate Bollinger Bands for a given price series
   """
   sma = data.rolling(window=period).mean()
   std = data.rolling(window=period).std()
   upper_band = sma + (std * std_dev)
   lower_band = sma - (std * std_dev)
   return upper_band.iloc[-1], sma.iloc[-1], lower_band.iloc[-1]


def calculate_bbp(price: float, upper_band: float, lower_band: float) -> float:
   """
   Calculate Bollinger Band Position (BBP)
   """
   return (price - lower_band) / (upper_band - lower_band)


def get_signal(rsi: float, bbp: float) -> str:
   """
   Determine buy/sell signal based on RSI and BBP values
   """
   if rsi <= 20 and bbp <= 0.15:
       return 'STRONG BUY'
   elif rsi <= 30 and bbp <= 0.2:
       return 'BUY'
   elif rsi <= 35 and bbp <= 0.3:
       return 'CONSIDER BUY'
   elif rsi >= 80 and bbp >= 0.85:
       return 'STRONG SELL'
   elif rsi >= 70 and bbp >= 0.8:
       return 'SELL'
   elif rsi >= 65 and bbp >= 0.7:
       return 'CONSIDER SELL'
   else:
       return 'HOLD'


def analyze_stock(symbol: str) -> Dict:
   """
   Analyze a single stock and return its indicators and signals
   """
   try:
       # Fetch stock data
       stock = yf.Ticker(symbol)
       hist = stock.history(period="1y")


       if hist.empty:
           return None


       # Calculate indicators
       rsi = calculate_rsi(hist['Close'])
       upper, middle, lower = calculate_bollinger_bands(hist['Close'])
       current_price = hist['Close'].iloc[-1]
       bbp = calculate_bbp(current_price, upper, lower)


       # Get signal
       signal = get_signal(rsi, bbp)


       return {
           'symbol': symbol,
           'rsi': round(rsi, 2),
           'bbp': round(bbp, 2),
           'price': round(current_price, 2),
           'signal': signal
       }
   except Exception as e:
       print(f"Error analyzing {symbol}: {str(e)}")
       return None


def analyze_stocks(symbols: List[str]) -> pd.DataFrame:
   """
   Analyze multiple stocks and return results as a DataFrame
   """
   results = []
   for symbol in symbols:
       result = analyze_stock(symbol)
       if result:
           results.append(result)


   if not results:
       return pd.DataFrame()


   df = pd.DataFrame(results)
   return df.sort_values(['rsi', 'bbp'], ascending=[False, False])