from setuptools import setup, find_packages


setup(
   name="stock_analyzer",
   version="0.1.0",
   packages=find_packages(),
   install_requires=[
       "yfinance>=0.2.36",
       "pandas>=2.0.0",
       "numpy>=1.24.0",
       "jinja2>=3.1.6",
       "urllib3<2.0.0",
   ],
   entry_points={
       "console_scripts": [
           "stock-analyzer=stock_analyzer.cli:main",
       ],
   },
   author="Your Name",
   author_email="your.email@example.com",
   description="A tool for analyzing stock technical indicators (RSI and Bollinger Bands)",
   long_description=open("README.md").read(),
   long_description_content_type="text/markdown",
   url="https://github.com/yourusername/stock_analyzer",
   classifiers=[
       "Programming Language :: Python :: 3",
       "License :: OSI Approved :: MIT License",
       "Operating System :: OS Independent",
   ],
   python_requires=">=3.9",
)
