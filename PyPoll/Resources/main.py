import csv
import os
election_data = os.path.join("election_data.csv")

candidates = []
total_votes = []
vote_counter = 0
perc_vote = []

with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csvheader = next(csvreader)

    for row in csvreader:
        vote_counter = vote_counter + 1
#create list of all candidates
        if row[2] not in candidates:
            candidates.append(row[2])
        else:
            continue
    print(candidates)


print("Election Results")
print("------------------")
print(f"Total Votes: {str(total_votes)}")
print("------------------")
for x in range(len(candidates)):
    print(f"{candidates[i]}: {str(perc_vote[i])} (str{str(num_votes[i])})")
print("-----------------")
print(f"Winner: {winner_name}")
print("--------------------")
