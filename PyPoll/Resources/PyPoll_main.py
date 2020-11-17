import csv
import os

with open('election_data.csv','r') as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
        print(row[1:5])
