import os
import csv

fhand = open('budget_data.csv')
csv_f = csv.reader(fhand)
fields = next(csv_f)
months = []
net_change = []
profit = []

for row in csv_f:
    months.append(row[0])
    profit.append(int(row[1]))

for i in range(len(profit)-1):
    net_change.append(profit[i+1]-profit[i])
    #print(months + net_change)
print(fields)
print(len(months))
