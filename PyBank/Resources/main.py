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
    average_change = sum(net_change) / len(net_change)
    max_increase = max(net_change)
    Max_date = str(months[net_change.index(max(net_change))])

    max_decrease = min(net_change)
    Min_date = str(months[net_change.index(min(net_change))])


print("Total months: ", len(months))
print("Average Change: $", average_change)
print("Greatest Increase: ", Max_date, max_increase)
print("Greatest Decrease: ", Min_date, max_decrease)
