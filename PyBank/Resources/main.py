import os
import csv

fhand = open('budget_data.csv')
csv_f = csv.reader(fhand)

for row in csv_f:
    print(row)
