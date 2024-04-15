import os
import csv

# Set the path to the input file

data_file_path = os.path.join("Resources", "election_data.csv")




# Initialize variables
total_votes = 0
candidate_votes = {}

# Read the input file


with open(data_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)  

    # Iterate over rows in the CSV
    for row in csv_reader:
        total_votes += 1
        candidate = row[2]

        # Update candidate votes tally
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Print total votes
print(f"Total Votes: {total_votes}")

# Print individual candidate results
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

# Determine the winner
winner = max(candidate_votes, key=candidate_votes.get)

# Print the winner
print(f"Winner: {winner}")

# Define the path for the output file
output_path = os.path.join("analysis", "election_results.txt")


output_dir = "analysis"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Write results to a text file
with open(output_path, "w") as output_file:
    output_file.write(f"Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        output_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")

print("Analysis results have been saved to election_results.txt.")
