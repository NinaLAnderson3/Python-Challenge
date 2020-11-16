import os
import csv

fhand = open('budget_data.csv')
csv_f = csv.reader(fhand)
months = []

for row in csv_f:
    months.append(row[0])
    print(len(months)-1)
