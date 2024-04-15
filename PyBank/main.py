import os
import csv

data_file_path = os.path.join("Resources", "budget_data.csv")


total_months = 0
net_total = 0
previous_month_profit_loss = 0
profit_loss_changes = []
greatest_increase_date = ""
greatest_decrease_date = ""
greatest_decrease_amount = 0
greatest_increase_amount = 0


#Open CSV
with open(data_file_path, 'r') as data_file:
    data_reader = csv.reader(data_file, delimiter=",")
    header = next(data_reader)

    # Iterate through rows and count months
    for row in data_reader:
        total_months += 1

        # Accumulate the profit/loss for the current month to the net total
        current_month_profit_loss = int(row[1])
        net_total += current_month_profit_loss

        # Compute the difference in profit/loss compared to the previous month
        if total_months > 1:
            profit_loss_diff = current_month_profit_loss - previous_month_profit_loss
            if greatest_increase_amount == 0:
                greatest_increase_amount = profit_loss_diff
            elif profit_loss_diff > greatest_increase_amount:
                greatest_increase_amount = profit_loss_diff
                greatest_increase_date = row[0]
            elif profit_loss_diff < greatest_decrease_amount:
                greatest_decrease_amount = profit_loss_diff
                greatest_decrease_date = row[0]
            profit_loss_changes.append(profit_loss_diff)

            # Adjust the records for the highest increase/decrease in profit/loss
            if profit_loss_diff > greatest_increase_amount:
                greatest_increase_amount = profit_loss_diff
                greatest_increase_date = row[0]
            elif profit_loss_diff < greatest_decrease_amount:
                greatest_decrease_amount = profit_loss_diff
                greatest_decrease_date = row[0]

        # Update the profit/loss from the previous month to the current month
        previous_month_profit_loss = current_month_profit_loss

# Determine the average variation in profit/loss
average_difference = sum(profit_loss_changes) / len(profit_loss_changes) if profit_loss_changes else 0

# Present the results in the terminal
print("Financial Analysis")
print("---------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_difference:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})")

output_dir = "analysis"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    
output_path = os.path.join("analysis", "analysis.txt")
with open(output_path, "w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("---------------------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${net_total}\n")
    output_file.write(f"Average Change: ${average_difference:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})\n")

print("Analysis results have been saved to analysis.txt.")