import os
import csv


csvpath = os.path.join('..','..','CWR-CLE-DATA-PT-01-2020-U-C', '03-Python','Homework03','Instructions', 'PyBank/Resources','budget_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    
    dates = []
    money = []
    
    
    for row in csvreader:
       dates.append(row[0])
       money.append(float(row[1]))
   
months = len(dates)
totalpnl = sum(money)
averagepnl = totalpnl/len(money)
    

maximum = max(money)
minimum = min(money)


data = list(zip(dates,money))



for x in data:
    if x[1] == maximum:
        maxdate= x[0]
    elif x[1] == minimum:
        mindate = x[0]


        

print("Financial Analysis")
print("----------------------")
print("Total Months: ", months)
print("Total: $" , totalpnl)
print("Average Change : $",format(averagepnl,".2f"))
print("Greatest Increase in Profits: ",maxdate,"(" + "$",maximum,")")
print("Greatest Decrease in Profits: ", mindate,"(" + "$",minimum,")")

    