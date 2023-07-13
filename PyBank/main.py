# Incorporated the csv module
import csv
import os

# Files to load and output (Remember to change these)

file_to_load = "Resources/budget_data.csv"
file_to_output = "Analysis/budget_analysis.txt"

# set variables, [(Total Months:) (Total:) (Average Change:) (Greatest Increase in Profits:) (Greatest Decrease in Profits:)]
total_months = 0
total = 0
total_change = 0
change_months = 0
greatest_increase = 0
greatest_decrease = 0


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as budget_data:
    reader = csv.reader(budget_data)
    
    header= next(reader)
    jan_row = next(reader)
    
    total_months = total_months + 1
    total = total + int(jan_row[1])

    prev_profit = int(jan_row[1])

    #Create for loop to read through the rows
    for row in reader:
        current_profit = int(row[1])
        total_months = total_months + 1
        total = total + current_profit

       
        change = current_profit - prev_profit
       
        total_change = total_change + change
        change_months = change_months + 1

        prev_profit = current_profit

        if change > greatest_increase:
            greatest_increase = change
            gip_date = row[0]
        if change < greatest_decrease:
            greatest_decrease = change
            gdp_date = row[0]

print(total_change / change_months)

output = f"""   
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total:,}
Average Change: ${total_change / change_months:,.2f}
Greatest Increase in Profits: {gip_date} (${greatest_increase:,})
Greatest Decrease in Profits: {gdp_date} (${greatest_decrease:,})
"""

print(output)

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)