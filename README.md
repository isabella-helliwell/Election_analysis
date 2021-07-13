# Election_analysis

## 1 Project Overview

      The aim of the project is to analyse the election data given in "election_results.csv" file for the
      following:
      1.1 The voter turnout for each county
      1.2 The percentage of votes from each county out of the total count
      1.3 The county with the highest turnout
      1.4 Each candidate and their votes and percentage vote
      1.5 The winning candidate and their votes and percentage vote
      Finally write the results into a text file 
## 2 Resources
      - Data source: elections_results.csv
      - Software: Python 3.7.6, Visual Studio Code version 1.58
## 3 Analysis
      
      The analysis are carried out using the csv file provided with the election data,
      iterating the data and counting the county votes and the candidate votes and printing
      out the results and saving it to a text file.
      This is done using Python codes.
      The coding aspect of the analysis is divided into 3 main sections. All of which is shown in 
      Parts1, 2 and 3 of the analysis section.
      
### 3.1 Analysis-Part 1
      
      The first part of the coding is to declare any variables, importing
      any libraries, modules, and creating any dictionaries and lists deem neccessary.
      The code below is showing the csv and os as imported modules, file_to_load and file_to_save
      as variables, and os.path. is a submodule that allows us to access files on different operating systems, and 
      the join fucntion will join the file path components together.
      We also need to create lista and dictionaries to hold the county and candidate names and their votes.
      Finaly, ther are some variables created for the winning_county and winning_candidate
      
      import csv
      import os
            
      file_to_load = os.path.join( "Resources", "election_results.csv") # Add a variable to load a file from a path.
           
      file_to_save = os.path.join("analysis", "election_analysis.txt")  # Add a variable to save the file to a path.
           
      total_votes = 0                                                   # Initialize a total vote counter.
           
      candidate_options = []                                            # Candidate Options and candidate votes
      candidate_votes = {}
            
      county_list=[]                                                    Create a county list and county votes dictionary.
      county_votes={}
  
      winning_candidate = ""                                            # Track the winning candidate, vote count and percentage
      winning_count = 0
      winning_count_1 = 0
      winning_percentage = 0
      winning_percentage_1 = 0
      winning_county = ""   
      
   
### 3.2 Analysis-part2

      The main partof the coding is to open the file we want to read the data from and analyse it by using
      iteration and calculations.
      
    with open(file_to_load) as election_data:                           # Read the csv and convert it into a list of dictionaries
    file_reader=csv.reader(election_data)
    header = next(file_reader)                                          # It will assume that the first row is the header in the file,
                                                                        # and will go to the next row, which will be the start position of the iteration
      
    for row in file_reader:                                             # Starting at the second row, for each row in the csv file 
        total_votes +=1                                                 # Adding 1 to the total vote counts, which is starting at 0
        county_name=row[1]                                              # Get the county name from each row, [1], tells the program that the county name is in column 2
        candidate_name=row[2]                                           # Get the candidate name from each row, [2], tells the program that the candidate name is in column 3
        if county_name not in county_list:                              # If county list is not a macth to any exsisting county name, add it to the county_list
            county_list.append(county_name)
            county_votes[county_name]= 0                                # Begin tracking the county's votes
        county_votes[county_name] += 1                                  # Add a vote to that county's vote count
        if candidate_name not in candidate_options:                     # The same is done for the candidate name and votes
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name] +=1  
        
### 3.3 Analysis-Part3

      The next part is to open a text file and write some analysis to it. however, in order to be able to write our analysis to this text file,
      we have to carry out some more iterations and loops inside this with statement.
      
      with open (file_to_save, "w") as txt_file:                  # we are opening the file_to_save wich is the "election_analysis.txt" file, and want to write to it "w"
          election_results = (f"Election Results"
               f"\n-----------------------------------\n"         # We are telling it to print out certain charactars and the value of the total votes that was calculated
               f"Total Votes: {total_votes:,}\n"                  # in part 1
               f"-----------------------------------\n"
               f"\nCounty Votes:\n")
           print(election_results)                                # The print function will print out in the VSC terminal what will be saved in the text file
           txt_file.write(election_results)    
      
     
  ![image](https://user-images.githubusercontent.com/85843030/125489238-c5238f24-6f2a-400e-b1ca-bc0a63f61777.png)


        
