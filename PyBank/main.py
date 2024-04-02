import csv
import os

# Path to the CSV file
file_path = "C:/Users/Joyjo/Downloads/Python-Challenge/Starter_Code/PyBank/Resources/budget_data.csv"

# assign variables
total_months = 0
net_total = 0
previous_profit_loss = 0
profit_loss_change = 0
profit_loss_changes = []
greatest_increase = {"date": "", "amount": 0}
greatest_decrease = {"date": "", "amount": 0}

# Read the CSV file
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #store header row
    csv_header = next(csvreader) 

    for row in csvreader:
         # Count total months
        total_months += 1

         # Calculate net total amount of Profit/Losses
        net_total += int(row[1])

        # Calculate change in profit/loss
        profit_loss_change = int(row[1]) - previous_profit_loss
        if previous_profit_loss != 0:
            profit_loss_changes.append(profit_loss_change)
        
        # Update previous profit/loss for the next iteration
        previous_profit_loss = int(row[1])

        # Find greatest increase in profits
        if profit_loss_change > greatest_increase["amount"]:
            greatest_increase["date"] = row[0]
            greatest_increase["amount"] = profit_loss_change

        # Find greatest decrease in profits
        if profit_loss_change < greatest_decrease["amount"]:
            greatest_decrease["date"] = row[0]
            greatest_decrease["amount"] = profit_loss_change

# Calculate the average change
average_change = sum(profit_loss_changes) / len(profit_loss_changes)

# Print the results to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")

# Export the results to a text file
output_folder = "analysis"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
output_file = os.path.join(output_folder, "financial_analysis.txt")
with open(output_file, "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("----------------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${net_total}\n")
    txt_file.write(f"Average Change: ${average_change:.2f}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n")
