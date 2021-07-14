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
           print(election_results)                                # The print function will print out in the VSC terminal what will be saved in the text file, see image1
           txt_file.write(election_results)    
      
   Image 1
  ![image](https://user-images.githubusercontent.com/85843030/125489238-c5238f24-6f2a-400e-b1ca-bc0a63f61777.png)


        Next is to create a for loop to get all the county names and their votes:
        
            for county_name in county_votes:                           # Iterating through the county list using county_name as the key and getting the values (votes)
                votes=county_votes[county_name]                            # Retrieving the total votes for each county using key(county_name), value=votes
                vote_percentage = float(votes) / float (total_votes)* 100     # Calculating the percentage of votes for each county
                county_results= (f"{county_name}:{vote_percentage :.1f}% ({votes:,})\n") #Assigning the results to county_results
                print(county_results)                                         # Printing it out to the terminal and saving it in the test file
                txt_file.write(county_results)
     
     The for loop goes through the county names and counts the votes, and writing the results out with the print statement and 
     writing the results in the text file.
    If we would to stop here the following output would be printed so far:
    
   Image 2
 ![image](https://user-images.githubusercontent.com/85843030/125515447-b846e2e0-2710-4cd6-8fc5-2ff2abdc57a4.png)
 

    
    Now that we know all the counties and their percentage vote and their total vote, we need to check to see
    which county has the largest turnout.
    This is done by an If statement:
                  if(votes>winning_count) and (vote_percentage>winning_percentage):   #check to make sure that the votes and %votes>0
                      winning_count=votes                                                 #assign winning_counts to thevalue of votes
                      winning_percentage = vote_percentage                                #assign winning percentage the value of vote_percentage
                      winning_county = county_name                                        #assign winning_county the name of the county it is reading
              county_winner= (f"\n-----------------------------------\n"                  #after the iterations through all the counties, the county_winner will
                              f"Largest County Turnout: {winning_county}\n"               #be assigned the value of the winning county
                              f"-----------------------------------\n")
              print(county_winner)                                                        #print out the county winner to the terminal with the formatting shown
              txt_file.write(county_winner)                                               #write the county_winner and it's formatting to the text file
    
    
    When the if statement is used first time, it will check so that the county votes and percentage votes are > 0. If this is the case,
    the if statement will asign the winning_count to the value of the votes.
    Since the if statement is nestled in the for loop, exsisting county read in the loop is compared to the previous one, and so on. 
    The out put at this point will look like Image 3
    
   Image 3 
  ![image](https://user-images.githubusercontent.com/85843030/125627638-7b7c1074-a44b-4954-aab6-6d3ce7404695.png)

  
  
    
