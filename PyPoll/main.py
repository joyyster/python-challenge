import os
import csv

#Path to the CSV file
election_data_csv = os.path.join("C:/Users/Joyjo/Downloads/Python-Challenge/Starter_Code/PyPoll/Resources/election_data.csv")

# variables
total_votes = 0
candidates = {}
winner = {"name": "", "votes": 0}

# Read the CSV file
with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row
    csv_header = next(csvreader)

    # Iterate through rows in the CSV file
    for row in csvreader:
        # Count total votes
        total_votes += 1

        # Record candidate votes
        candidate_name = row[2]
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

        # Update winner
        if candidates[candidate_name] > winner["votes"]:
            winner["name"] = candidate_name
            winner["votes"] = candidates[candidate_name]

# Print the results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner['name']}")
print("-------------------------")

# Export the results to a text file
output_folder = "analysis"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
output_file = os.path.join(output_folder, "election_results.txt")
with open(output_file, "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("-------------------------\n")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        txt_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Winner: {winner['name']}\n")
    txt_file.write("-------------------------\n")