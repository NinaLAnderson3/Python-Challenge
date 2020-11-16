import os
import csv

budget_data = os.path.join('budget_data.csv')

total_months = 0
profit_loss = 0
value = 0
months = []
profits = []

with open(budget_data, newline='',) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    csv_header = next(csvreader)
    first_row = next(csvreader)
    total_months +=1
    profit_loss += int(first_row[1])
    value = int(first_row[1])

    for row in csvreader:
        months.append(row[0])
        net = int(row[1])-value
        profits.append(net)
        value = int(row[1])

        #total_months += 1
        profit_loss = profit_loss+int(row[1])

        greatest_increase = max(profits)
        gain = profits.index(greatest_increase)
        best_date = months[gain]

        max_decrease = min(profits)
        loss = profits.index(max_decrease)
        worst_date = months[loss]

        avg_change = sum(profits)/len(profits)


print("Total months: ", len(months)+1)
print("Average Change: $", avg_change)
print("Total is:", profit_loss)
print("Greatest Increase: ", best_date, greatest_increase)
print("Greatest Decrease: ", worst_date, max_decrease)

output = open("analysis.txt","w")

line1 = "Financial Analysis"
line2 = "----------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(profit_loss)}")
line5 = str(f"Average Change: ${str(round(avg_change))}")
line6 = str(f"Greatest Increase in Profits: {best_date}${str(greatest_increase)}")
line7 = str(f"Greatest decrease in profits: {worst_date}(${str(max_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4, line5, line6, line7))
