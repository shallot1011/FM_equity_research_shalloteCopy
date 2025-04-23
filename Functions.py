# Profitability Ratios

#Gross margin: 
def gross_margin(gross_profit,revenue):
    return gross_profit/revenue

#EBITDA Margin
def ebitda_margin(ebitda,revenue):
    return ebitda/revenue

#ROE
def roe(net_income,total_equity_ave):
    return net_income/total_equity_ave

#EPS 
def eps(net_income, shares_outstanding):
    return net_income / shares_outstanding


# Growth ratios

#EPS Growth
def eps_growth(previous_eps,current_eps):
    if previous_eps == 0:
        return "Cannot calculate growth"
    growth = ((current_eps - previous_eps)/previous_eps)* 100
    return round(growth,2) #round -> rounds to 2 decimal places



#Valuation Mutiples

# Dividend Yield
def dividend_yield(dividend,last_price):
    return dividend/last_price

#PE ratio

def pe_ratio(last_price, eps):
    return last_price / eps

#Enterprise multiple
def ev_ebitda(ev,ebitda):
    return ev/ebitda


#leverage

# Debt to equity ratio
def debt_equity(total_debt,total_equity_current):
    return total_debt/total_equity_current

