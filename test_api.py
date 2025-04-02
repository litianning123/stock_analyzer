from stock_analyzer.analyzer import analyze_stocks


# Test with a few tech stocks
symbols = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META']
results = analyze_stocks(symbols)


# Print results
print("\nTest Results:")
print("=" * 80)
print(f"{'Symbol':<10} {'RSI':<10} {'BBP':<10} {'Price':<10} {'Signal':<15}")
print("-" * 80)


for _, row in results.iterrows():
   print(f"{row['symbol']:<10} {row['rsi']:<10.2f} {row['bbp']:<10.2f} {row['price']:<10.2f} {row['signal']:<15}")