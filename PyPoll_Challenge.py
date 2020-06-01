# Add our dependencies
import csv
import os
# Assign a variable to load a file from the path
file_to_load=os.path.join("Resources/election_results.csv")
#Assign a variable to save the file to a path
file_to_save=os.path.join("analysis","election_analysis.txt")

# Initialize a total vote counter.
total_votes=0

#Candidate Options and Candidate Votes
candidate_options=[]
candidate_votes={}

#Track the winning candidate, vote count, and percentage.
winning_candidate=""
winning_count=0
winning_percentage=0

#Create a list containing the name of the counties that voted.
counties=[] 
#Create a dictionary, the key is the county name, the value is votes cast in that county.
county_vote_tracker={}
#Create an empty string to hold the county with the highest turn out, and a variable hold the number of votes for the county with the largest turnout
largest_county_turnout=""
highest_county_votes=0

#Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data) 
    #Read the header row.  
    headers=next(file_reader) 

    #Loop through all rows in the CSV file. 
    for row in file_reader:
        # Add to the total vote count.
        total_votes+=1
        #Get the candidate name from each row.
        candidate_name=row[2]

        #If candidate does not match any existing candidate add it to the candidate list.
        if candidate_name not in candidate_options:
            #Add it to the list of candidates
            candidate_options.append(candidate_name)
            #Begin tracking that candidate's vote count
            candidate_votes[candidate_name]=0
        #Add a vote to the candidate's vote count
        candidate_votes[candidate_name]+=1 

        #Get the name of the county from each row. 
        county_name=row[1]
        #Create an if statement checking if county name is within the list of county names 
        if county_name not in counties:
            #Add it to the list of counties
            counties.append(county_name)
            #Begin tracking the county's vote count.
            county_vote_tracker[county_name]=0
        #Add a vote to the county's vote count.
        county_vote_tracker[county_name]+=1

#Save the results to our text file.
with open(file_to_save,"w") as txt_file:
#Print the final vote count to the terminal, followed by the header for county votes.
    election_results=(
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\nCounty Votes:\n")    
    print(election_results, end="")
    #Save the final vote count to the text file.
    txt_file.write(election_results)
    #Iterate through the county name list.
    for county in counties:
        #Retrieve the vote count of each county.
        cvotes=county_vote_tracker[county]
        #Calculate the percentage of votes attributed to each county.
        county_vote_percentage=float(cvotes)/float(total_votes)*100
        #Create a variable containing how the county results are to printed in the output file and terminal.
        county_results= (
            f"{county}: {county_vote_percentage:.1f}% ({cvotes:,})\n")
        
        #Print each county's voter count and percentage to the terminal
        print(county_results)
        #Save the county's results to our text file.
        txt_file.write(county_results)
        #Determine the highest county turnout.
        if(cvotes>highest_county_votes):
            highest_county_votes=cvotes
            largest_county_turnout=county
    #Print largest county's results to the terminal
    largest_county_summary=(
        f"\n-------------------------\n"
        f"Largest County Turnout: {largest_county_turnout}\n"
        f"-------------------------\n")
    print(largest_county_summary)
    #Save the largest county turnout results to the text file.
    txt_file.write(largest_county_summary)
            
    #Iterate through the candidate list.
    for candidate in candidate_votes:
        #Retrieve vote count of a candidate
        votes=candidate_votes[candidate]
        #Calculate the percentage of votes
        vote_percentage=float(votes)/float(total_votes)*100
        candidate_results= (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        #Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #Save the candidate results to our text file.
        txt_file.write(candidate_results)
        #Determine winning vote count, winning percentage, and candidate.
        if(votes>winning_count) and (vote_percentage>winning_percentage):
            winning_count=votes
            winning_percentage=vote_percentage
            winning_candidate=candidate

    #Print the winning candidates' results to the terminal.
    winning_candidate_summary=(
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
        
    print(winning_candidate_summary)
    #Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
            

        











    