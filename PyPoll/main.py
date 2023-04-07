#import libraries
import pandas as pd
from pathlib import Path


#imports and reads csv
csvPath = Path(r"PyPoll\Resources\election_data.csv")
pyPoll_df = pd.read_csv(csvPath)


#defines variables
totalVotes = len(pyPoll_df)
charles = 0
diana = 0
raymon = 0
winner = ""


#Loops through csv "Candidate" column. If a candidate's name is found, adds +1 vote to count
for i in pyPoll_df["Candidate"]:
    if i == "Charles Casper Stockham":
        charles += 1
    elif i == "Diana DeGette":
        diana += 1
    elif i == "Raymon Anthony Doane":
        raymon += 1


#Checks which candidate received the most vote and updates "winner" variable
if charles > diana and charles > raymon:
    winner = "Charles Casper Stockham"
elif diana > charles and diana > raymon:
    winner = "Diana DeGette"
elif raymon > charles and raymon > diana:
    winner = "Raymon Anthony Doane"


#More variables to display percent of overall votes in the final output
charlesPercent = round((charles / totalVotes) * 100, 3)
dianaPercent = round((diana / totalVotes) * 100, 3)
raymonPercent = round((raymon / totalVotes) * 100, 3)


#Defines a function to easily reference and call output later on
def pollAnalysis():
    print("Election Results\n------------------")
    print(f"Total Votes: {totalVotes}\n------------------")
    print(f"Charles Casper Stockham: {charlesPercent}% ({charles})")
    print(f"Diana DeGette: {dianaPercent}% ({diana})")
    print(f"Raymon Anthony Doane: {raymonPercent}% ({raymon})\n------------------")
    print(f"Winner: {winner}\n------------------")


#Prints the output to console and saves it as a text file
# Ran into same problem as PyBank output. 
# Could not figure out how to easily write output from "pollAnalysis()" function
pollAnalysis()
with open("PyPoll\Analysis\PyPollOutput.txt", "w") as f:
    f.write("Election Results\n------------------")
    f.write(f"\nTotal Votes: {totalVotes}\n------------------")
    f.write(f"\nCharles Casper Stockham: {charlesPercent}% ({charles})")
    f.write(f"\nDiana DeGette: {dianaPercent}% ({diana})")
    f.write(f"\nRaymon Anthony Doane: {raymonPercent}% ({raymon})\n------------------")
    f.write(f"\nWinner: {winner}\n------------------")