# Use this to only find data fields in yfinance
import yfinance as yf
ticker = yf.Ticker("RHC.AX")

# Income statement fields
print(ticker.financials.index)
print(ticker.financials.columns)

# Balance sheet fields
print(ticker.balance_sheet.index)

# Cashflow statement fields
print(ticker.cashflow.index)


# All .info fields
print(ticker.info.keys())