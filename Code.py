import matplotlib as mpl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
plt.style.use('seaborn-whitegrid')
DIS=pd.read_csv("DIS.csv")
x=np.linspace(2,13356,13356)
plt.plot(x,DIS['Close'])
plt.ylabel('Closing price')
plt.title('Value of DIS stock over time')
plt.savefig("Value of DIS over time.jpeg")

mpl.style.use('_mpl-gallery')
gross = pd.read_csv("disney_movies_total_gross.csv", parse_dates=["release_date"])
stocks = pd.read_csv("DIS.csv")

grossX = gross.loc[:,"release_date"]
grossY = gross.loc[:,"inflation_adjusted_gross"]

stocksX = stocks.loc[:,"Date"]
stocksY = stocks.loc[:,"Adjusted Close"]

print(gross)
print(stocks)

figBoxOfficeOverTime = mpl.pyplot.figure()
mpl.pyplot.rcParams["figure.figsize"] = [10.50, 3.50]
mpl.pyplot.plot(grossX, grossY)
mpl.pyplot.title("Disney Box Office Performance Adjusted for Inflation")
mpl.pyplot.xlabel("Date (in years)")
mpl.pyplot.ylabel("Money (in billions of dollars)")
figBoxOfficeOverTime.savefig('Fig1.png', dpi=300, bbox_inches='tight')
mpl.pyplot.show()
files.download('Fig1.png')

i = 0
for r in gross.loc[:,"release_date"]:
  if r.year < 1970:
    gross = gross.drop(gross.index[i])
  else:
    i+=1
display(gross)

grossX = gross.loc[:,"release_date"]
grossY = gross.loc[:,"inflation_adjusted_gross"]

stocks_trimmed = pd.DataFrame(columns= ['Date', 'Low', 'Open', 'Volume', 'High', 'Close', 'Adjusted Close'])
df_to_plot = pd.DataFrame(columns= ['Date', 'Inflation Adjusted Gross', 'Adjusted Close'])

for date in grossX:
  year = date.year;
  month = date.month;
  day = date.day
  day_filler = ''
  if day < 10:
    day_filler = '0'
  month_filler = ''
  if month < 10:
    month_filler = '0'
  date_string = day_filler + str(day) + "-" + month_filler + str(month) + "-" + str(year)
  stockRow = stocks.loc[stocks['Date'] == date_string]
  grossRow = gross.loc[gross['release_date'] == date]
  if stockRow.size > 0:
    newRow = pd.DataFrame([[date, grossRow.at[grossRow.index[0],'inflation_adjusted_gross'], stockRow.at[stockRow.index[0],'Adjusted Close']]], columns= ['Date', 'Inflation Adjusted Gross', 'Adjusted Close'])
    df_to_plot = pd.concat([df_to_plot, newRow], ignore_index=True)

display(df_to_plot)

figDouble = mpl.pyplot.figure()
mpl.pyplot.rcParams["figure.figsize"] = [21, 3.50]
mpl.pyplot.plot(grossX, grossY)
mpl.pyplot.subplot(1,2,1)
mpl.pyplot.plot(df_to_plot['Date'], df_to_plot['Inflation Adjusted Gross'])
mpl.pyplot.title("Box Office Value Overtime")
mpl.pyplot.xlabel("Date")
mpl.pyplot.ylabel("Box Office Value (in Billions of Dollars)")

mpl.pyplot.subplot(1,2,2)
mpl.pyplot.plot(df_to_plot['Date'], df_to_plot['Adjusted Close'])
mpl.pyplot.title("Stocks Closing Price Overtime")
mpl.pyplot.xlabel("Date")
mpl.pyplot.ylabel("Adjusted Stock Value")

mpl.pyplot.show()
figDouble.savefig('Fig2.png', dpi=300, bbox_inches='tight')
files.download('Fig2.png')

figScatter = mpl.pyplot.figure()
mpl.pyplot.rcParams["figure.figsize"] = [10.50, 3.50]
mpl.pyplot.scatter(df_to_plot['Inflation Adjusted Gross'], df_to_plot['Adjusted Close'])
mpl.pyplot.title("Box Office Value vs. Stocks Closing Price")
mpl.pyplot.xlabel("Box Office Value (in billions of dollars)")
mpl.pyplot.ylabel("Adjusted Closing Price")
mpl.pyplot.show()
figScatter.savefig('Fig3.png', dpi=300, bbox_inches='tight')
files.download('Fig3.png')
