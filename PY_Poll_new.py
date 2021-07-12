# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Set total votes = 0, so that each time we open the file and start counting the votes, the count
    # starts with 0
total_votes = 0   
candidate_options = [] # create a list
candidate_votes={} #create a dictionary
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)  # Read and print the header row.
    headers = next(file_reader) # this code skips the first row,( header row)
    print(f"{headers} \n") # this will print out the row that we just skipped, just to check for ourselves
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0 # candidates are used as key with this statement, and we are
                                                #setting each candidate's vote count to 0
        candidate_votes[candidate_name] +=1
        #print(row) #prints out each row
        #print(total_votes)#prints out each row and add 1, ex, 2,3,4,5,....369712.
        #candidate_options.append(candidate_name)
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage=float(votes)/float(total_votes)*100
    #print(f"{candidate_name} : received {vote_percentage:.1f}% of votes")


#print(candidate_votes)
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_counts = votes
        print(f"{votes} : is it counting?")
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")




winning_candidate_summary = (  
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_counts:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
#print (candidate_options)
#winning candidate and winning count tracker
