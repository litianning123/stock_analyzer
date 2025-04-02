# Stock Analyzer


A Python package for analyzing stock technical indicators (RSI and Bollinger Bands) and generating trading signals.


## Installation


1. Clone the repository:
```bash
git clone https://github.com/litianning123/stock_analyzer.git
cd stock_analyzer
```


2. Create and activate a virtual environment:
```bash
# Create virtual environment
python3 -m venv venv


# On macOS/Linux:
source venv/bin/activate


# On Windows:
venv\Scripts\activate
```


3. Install the package:
```bash
pip install -e .
```


## Usage


### Command Line Interface


The package provides a command-line interface that can be used in two ways:


1. Analyze multiple stocks from a file:
```bash
stock-analyzer
```
This will read stock symbols from `stocks.txt` by default.


2. Analyze a single stock:
```bash
stock-analyzer --symbol AAPL
```


3. Use a custom symbols file:
```bash
stock-analyzer --symbols my_stocks.txt
```


### Python API


You can also use the package in your Python code:


```python
from stock_analyzer.analyzer import analyze_stocks


# Analyze multiple stocks
symbols = ['AAPL', 'MSFT', 'GOOGL']
results = analyze_stocks(symbols)
print(results)
```


## Features


- Calculates RSI (Relative Strength Index)
- Calculates Bollinger Bands and BBP (Bollinger Band Position)
- Provides trading signals (STRONG BUY/BUY/CONSIDER BUY/SELL/STRONG SELL/CONSIDER SELL/HOLD)
- Color-coded output for easy signal identification
- Supports both file-based and single-symbol analysis
- Sorts results by RSI and BBP values


## Trading Signals


The tool generates trading signals based on the following conditions:
- **STRONG BUY** (Bright Green): RSI <= 20 and BBP <= 0.15
- **BUY** (Green): RSI <= 30 and BBP <= 0.2
- **CONSIDER BUY** (Cyan): RSI <= 35 and BBP <= 0.3
- **SELL** (Red): RSI >= 70 and BBP >= 0.8
- **STRONG SELL** (Bright Red): RSI >= 80 and BBP >= 0.85
- **CONSIDER SELL** (Magenta): RSI >= 65 and BBP >= 0.7
- **HOLD**: All other conditions


## Requirements


- Python 3.9 or higher
- Required packages:
 - yfinance >= 0.2.36
 - pandas >= 2.0.0
 - numpy >= 1.24.0
 - jinja2 >= 3.1.6


## License


This project is licensed under the MIT License - see the LICENSE file for details.


## Disclaimer


This tool is for educational and informational purposes only. The trading signals it generates should not be considered as financial advice. Always do your own research and consult with financial professionals before making investment decisions.
