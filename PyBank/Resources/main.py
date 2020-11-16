import os
import csv

#define variables
month_count = 0
months = []
total_rev = 0
current_rev = 0
last_rev = 0
rev_change = 0
changes = []
budgetData_csv = os.path.join('budget_data.csv')

with os.path.join('budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    print(header)
