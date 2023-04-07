#Import libraries
import pandas as pd
from pathlib import Path


#Import and read csv
csvPath = Path(r"PyBank\Resources\budget_data.csv")
pyBank_df = pd.read_csv(csvPath)


#Counts total rows taking headers into consideration
totalMonths = len(pyBank_df)
#Sums the 'Profit/Losses' column
totalChange = pyBank_df["Profit/Losses"].sum()
#Computes differences in the P/L column, takes average, then rounds to 2 decimals
averageChange = round((pyBank_df["Profit/Losses"].diff()).mean(), 2)
#Computes differences in the P/L column & takes max. Converted to Int to match output
greatestIncInProfits = int((pyBank_df["Profit/Losses"].diff()).max())
#Computes differences in the P/L column & takes min. Converted to Int to match output
greatestDecInProfits = int((pyBank_df["Profit/Losses"].diff()).min())


#Defines all of my output for easier access/calling
def financialAnalysis():
    print("Financial Analysis \n------------------")
    print(f"Total Months: {totalMonths}")
    print(f"Total: ${totalChange}")
    print(f"Average Change: ${averageChange}")
    print(f"Greatest Increase in Profits: ${greatestIncInProfits}")
    print(f"Greatest Decrease in Profits: ${greatestDecInProfits}")


#Writes output to console & saves as text file. 
# Could not figure out how to capture output of financialAnalysis()
# as a writable variable so as not to write all the "f.write" lines
financialAnalysis()
with open("PyBank\Analysis\PyBankOutput.txt", "w") as f:
    f.write("Financial Analysis \n------------------")
    f.write(f"\nTotal Months: {totalMonths}")
    f.write(f"\nTotal: ${totalChange}")
    f.write(f"\nAverage Change: ${averageChange}")
    f.write(f"\nGreatest Increase in Profits: ${greatestIncInProfits}")
    f.write(f"\nGreatest Decrease in Profits: ${greatestDecInProfits}")
