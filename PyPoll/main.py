# Incorporated the csv module
import csv
import os

# Files to load and output (Remember to change these)
file_to_load = os.path.join("Resources", "election_data.csv")

total_votes = 0

candiate_names = [] # empty list
candidate_votes = {} # empty dictionary - key:value pair

winning_candidate = ""
winning_count = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    for row in reader:
        total_votes = total_votes + 1

        candidate_name = row[2]

        check if candidate_name is in the names list
        if yes - add 1 to the candidate's vote count in the dictionary
        if no - add the candidate_name to the names list and set the new candidate's vote count to 1



print(total_votes)