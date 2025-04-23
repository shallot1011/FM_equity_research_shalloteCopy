import yfinance as yf

import Functions




# Take user input for ticker
TICKER = input('Enter a stock ticker (e.g. BHP.AX): ').upper()

try:
    # Get stock information
    stock = yf.Ticker(TICKER)
    stock_prices = stock.history(period="10y")
    stock_info = stock.info
    stock_financials = stock.financials
    stock_balance_sheet = stock.balance_sheet

    # Extract relevant information
    revenue = stock_financials.loc["Total Revenue"].iloc[0]
    gross_profit = stock_financials.loc["Gross Profit"].iloc[0]
    ebitda = stock_financials.loc["EBITDA"].iloc[0]
    total_equity_ave = (stock_balance_sheet.loc["Stockholders Equity"].iloc[0] + stock_balance_sheet.loc["Stockholders Equity"].iloc[1]) / 2
    total_equity_current = stock_balance_sheet.loc["Stockholders Equity"].iloc[0]
    total_debt = stock_balance_sheet.loc["Total Debt"].iloc[0]
    ev = dividend = stock_info['enterpriseValue']
    last_price = stock_prices['Close'].iloc[-1]
    net_income = stock_financials.loc["Net Income"].iloc[0]
    dividend = stock_info['lastDividendValue']
    shares_outstanding = stock_info['sharesOutstanding']


    gross_margin = Functions.gross_margin(gross_profit,revenue)
    ebitda_margin = Functions.ebitda_margin(ebitda,revenue)
    roe = Functions.roe(net_income,total_equity_ave)
    dividend_yield = Functions.dividend_yield(dividend,last_price) * 100
    eps = Functions.eps(net_income, shares_outstanding)
    pe_ratio = Functions.pe_ratio(last_price, eps)
    ev_ebitda = Functions.ev_ebitda(ev,ebitda)
    debt_equity = Functions.debt_equity(total_debt,total_equity_current)

    


except Exception as e:
    print(f"Error: {e}")

print(f"Chosen Stock: {TICKER} \nLast Share Price: {last_price:.2f} \nPE Ratio: {pe_ratio:.2f} \nDividend Yield: {dividend_yield:.2f}% \nEPS: {eps:.2f} \nGross Margin: {gross_margin:.2f}% \nEBITDA Margin: {ebitda_margin:.2f}% \nROE: {roe:.2f}% \nEV/EBITDA: {ev_ebitda:.2f} \nDebt/Equity: {debt_equity:.2f}")
