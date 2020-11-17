import csv
import os

#handle
election_data = os.path.join("election_data.csv")

#created lists to hold candidates, number of votes and perecntages
candidates = []
num_votes = []
percent_votes = []
total_votes = 0

#read file data
with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #define header so calculations skip first record
    header = next(csvreader)
#count total number of votes (each record is a vote)
    for row in csvreader:
        total_votes += 1
#create list of candidates and add number of votes associated with each
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1
#print(candidates, num_votes)
#calculate percentages and add to list of percentages
    for votes in num_votes:
        percent = round((votes/total_votes) * 100,3)
        percent_votes.append(percent)
    #print(percent_votes)

#define winning number of votes and name associated with maximum num of votes
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]
    #print(winning_candidate, num_votes[0])


print("Election Results")
print("------------------")
print(f"Total Votes: {str(total_votes)}")
print("------------------")
for x in range(len(candidates)):
    print(f"{candidates[x]}: {str(percent_votes[x])}% ({str(num_votes[x])})")
print("-----------------")
print(f"Winner: {winning_candidate}{winner}")
print("--------------------")

#create output
newfile = open("PyPoll_analysis.txt","w")
line1 = "Election Results"
line2 = "-----------------"
line3 = str(f'Total Votes: {str(total_votes)}')
line4 = str("--------------")
newfile.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range (len(candidates)):
    line = str(f'{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})')
    newfile.write('{}\n'.format(line))
line5 = "----------------"
line6 = str(f"Winner: {winning_candidate}")
line7 ="----------------"
newfile.write('{}\n{}\n{}\n'.format(line5, line6, line7))
