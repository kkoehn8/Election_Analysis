#The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of botes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.

import csv
# from email import headerregistry
import os

#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize a total vote counter
total_votes = 0

#Candidate options
candidate_options = []

#Create candidate votes dictionary
candidate_votes = {}

#Winning count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0


#Open the election results and read the file.
with open(file_to_load) as election_data:

    #To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    #Read the header row.
    headers = next(file_reader)
    
    #Print each row in the CSV tile
    for row in file_reader:
        #Add to the total vote count
        total_votes +=1

        #Print the candidate name from each row
        candidate_name = row[2]

        #If the candidate does not match any existing candidate...

        if candidate_name not in candidate_options:
            #Add it to the list of candidates.
            candidate_options.append(candidate_name)

            #Begin tracking that candidate's vote
            candidate_votes[candidate_name] = 0

        #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        #Determine the percentage of botes for each candidate by looping through the counts
for candidate_name in candidate_votes:
    #Retrieve vote county of a candidate
    votes = candidate_votes[candidate_name]

    #calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) *100

    #To do: print out each candidate's name, vote county, and percentage of votes to the terminal
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


    
    #Determine winning vote count and candidate
    #Determine if the votes are greater than the winning count

    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #If true then set winning_count = votes and winning_percentage = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        #And set the winning_candidate equpt to the candidate's name
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"----------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"------------------------------------\n")
print(winning_candidate_summary)



#print(candidate_votes)







