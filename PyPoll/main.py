import csv
import os

# Files to load and output (Remember to change these)
file_to_load = "Resources/election_data.csv"
file_to_output = "Analysis/election_analysis.txt"

# Variables for analysis
total_votes = 0
candidate_names = []  # empty list
candidate_votes = {}  # empty dictionary - key:value pair

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # Iterate over each row in the CSV file
    for row in reader:
        # Count the total number of votes
        total_votes += 1

        candidate_name = row[2]

        # Check if the candidate's name is already in the candidate_names list
        if candidate_name not in candidate_names:
            # Add the candidate to the candidate_names list
            candidate_names.append(candidate_name)

            # Begin tracking that candidate's voter count
            candidate_votes[candidate_name] = 0

        # Increment the vote count for the candidate
        candidate_votes[candidate_name] += 1

# Calculate the percentage of votes and determine the winner
winner = ""
winner_votes = 0

output_results = []

for candidate in candidate_votes:
    votes = candidate_votes[candidate]
    percentage = (votes / total_votes) * 100

    output_results.append(f"{candidate}: {percentage:.2f}% ({votes})")

    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

output_results.append("")
output_results.append("Winner: " + winner)
output_results.append("Total Votes: " + str(total_votes))
output_results.append("Candidate Votes: " + str(candidate_votes))
output_results.append("Candidate Names: " + str(candidate_names))

# Write the results to the output file
with open(file_to_output, "w") as analysis_file:
    for line in output_results:
        analysis_file.write(line + "\n")

# Print the results to the console
for line in output_results:
    print(line)