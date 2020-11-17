import csv
import os

election_data = os.path.join("election_data.csv")

candidates = []
num_votes = []
percent_votes = []
total_votes = 0

with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        total_votes += 1

        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1
#print(candidates, num_votes)
    for votes in num_votes:
        percent = round((votes/total_votes) * 100,2)
        percent_votes.append(percent)
    #print(percent_votes)

    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]

    print(winning_candidate, num_votes[0])


#print("Election Results")
#print("------------------")
#print(f"Total Votes: {str(total_votes)}")
#print("------------------")
#for x in range(len(candidates)):
#    print(f"{candidates[i]}: {str(perc_vote[i])} (str{str(num_votes[i])})")
#print("-----------------")
#print(f"Winner: {winner_name}")
#print("--------------------")
