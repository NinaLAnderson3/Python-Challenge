import os
import csv

budgetData_csv = os.path.join('budget_data.csv')

with os.path.join('budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
