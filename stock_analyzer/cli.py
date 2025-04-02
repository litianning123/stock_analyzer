"""
Command-line interface for the stock analyzer
"""


import sys
import argparse
from pathlib import Path
from .analyzer import analyze_stocks


def color_text(text: str, signal: str) -> str:
   """
   Add ANSI color codes to text based on signal
   """
   if signal == 'STRONG BUY':
       return f'\033[92m{text}\033[0m'  # Bright green
   elif signal == 'BUY':
       return f'\033[32m{text}\033[0m'  # Green
   elif signal == 'CONSIDER BUY':
       return f'\033[36m{text}\033[0m'  # Cyan
   elif signal == 'STRONG SELL':
       return f'\033[91m{text}\033[0m'  # Bright red
   elif signal == 'SELL':
       return f'\033[31m{text}\033[0m'  # Red
   elif signal == 'CONSIDER SELL':
       return f'\033[35m{text}\033[0m'  # Magenta
   return text


def read_symbols(file_path: str) -> list:
   """
   Read stock symbols from a file
   """
   try:
       with open(file_path, 'r') as f:
           return [line.strip() for line in f if line.strip()]
   except Exception as e:
       print(f"Error reading symbols file: {str(e)}")
       return []


def print_results(df):
   """
   Print analysis results with proper formatting
   """
   if df.empty:
       print("No valid results to display.")
       return


   # Print header
   print("\nResults (sorted by RSI and BBP):")
   print("=" * 80)
   print(f"{'Symbol':<10} {'RSI':<10} {'BBP':<10} {'Price':<10} {'Signal':<15}")
   print("-" * 80)


   # Print data rows
   for _, row in df.iterrows():
       signal = color_text(row['signal'], row['signal'])
       print(f"{row['symbol']:<10} {row['rsi']:<10.2f} {row['bbp']:<10.2f} {row['price']:<10.2f} {signal:<15}")


   # Print interpretation guide
   print("\nInterpretation Guide:")
   print("RSI > 70: Overbought")
   print("RSI < 30: Oversold")
   print("BBP > 0.8: Near upper band")
   print("BBP < 0.2: Near lower band")
   print("\nSignal Conditions:")
   print(color_text("STRONG BUY: RSI <= 20 and BBP <= 0.15", "STRONG BUY"))
   print(color_text("BUY: RSI <= 30 and BBP <= 0.2", "BUY"))
   print(color_text("CONSIDER BUY: RSI <= 35 and BBP <= 0.3", "CONSIDER BUY"))
   print(color_text("SELL: RSI >= 70 and BBP >= 0.8", "SELL"))
   print(color_text("STRONG SELL: RSI >= 80 and BBP >= 0.85", "STRONG SELL"))
   print(color_text("CONSIDER SELL: RSI >= 65 and BBP >= 0.7", "CONSIDER SELL"))
   print("HOLD: All other conditions")


def main():
   """
   Main entry point for the command-line interface
   """
   parser = argparse.ArgumentParser(description='Analyze stocks using RSI and Bollinger Bands')
   parser.add_argument('--symbols', '-s', default='stocks.txt',
                     help='Path to file containing stock symbols (default: stocks.txt)')
   parser.add_argument('--symbol', '-t', help='Single stock symbol to analyze')


   args = parser.parse_args()


   if args.symbol:
       symbols = [args.symbol]
   else:
       symbols = read_symbols(args.symbols)


   if not symbols:
       print("No symbols provided. Please specify symbols using --symbol or --symbols")
       sys.exit(1)


   df = analyze_stocks(symbols)
   print_results(df)


if __name__ == '__main__':
   main()