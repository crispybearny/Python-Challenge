import os
import pandas as pd


#Format Currency Function (Downloaded from Web)
def as_currency(amount):
    if amount >= 0:
        return '${:,.2f}'.format(amount)
    else:
        return '-${:,.2f}'.format(-amount)


#Create two DataFrames
budgetData = pd.read_csv("budget_data.csv")
deltaGross = budgetData["Profit/Losses"].diff()


#GetResults
h1Month=budgetData["Date"].count()
h2Money=budgetData["Profit/Losses"].sum()
h3Mean=deltaGross.mean()
h4Max = str(as_currency(deltaGross.max()))+" on " +str(budgetData.loc[deltaGross.idxmax(),"Date"])
h4Min = str(as_currency(deltaGross.min()))+" on " +str(budgetData.loc[deltaGross.idxmin(),"Date"])
#h4Max = str(budgetData["Profit/Losses"].max())+" on " +str(budgetData.loc[budgetData["Profit/Losses"].idxmax(),"Date"])


#Print results to Screen
print("\n\nFinancial Analysis")
print("______________________________________________________")
print (f'Total Months:  {h1Month}')
print (f'Total Net Revenue:  {as_currency(h2Money)}')
print (f'Average Delta:      {as_currency(h3Mean)}')
print (f'Highest Delta:      {h4Max}')
print (f'Lowest  Delta       {h4Min}')
print("______________________________________________________")

#Print results to file
ToFile= open("GlennResults.txt","w+")

ToFile.write("Financial Analysis\r\n")
ToFile.write("______________________________________________________\r\n")
ToFile.write (f'Total Months:  {h1Month}\r\n')
ToFile.write (f'Total Net Revenue:  {as_currency(h2Money)}\r\n')
ToFile.write (f'Average Delta:      {as_currency(h3Mean)}\r\n')
ToFile.write (f'Highest Delta:      {h4Max}\r\n')
ToFile.write (f'Lowest  Delta       {h4Min}\r\n')
ToFile.write("______________________________________________________\r\n")

ToFile.close()
