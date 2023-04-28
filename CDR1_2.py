import pandas as pd
import sys

input_file = sys.argv[1]

df = pd.read_csv(input_file)

#Input positions to write in the command window:
positions = input("Enter a comma-separated list of positions: ") 
"""
Standard treshold: 4% for CDR1 and CDR2
CDR1: 35A
CDR2: 52B

"""
positions = positions.split(",") 
positions = [pos.strip() for pos in positions]  # Enable to have space between the positions in the input
parts = {} #Short sequences added here

for pos in positions: #Iterates over selected positions
    part = df.loc[df[pos] == '-'] #Selects all the columns where values in pos is equal to '-' and put the sequences in 'part'
    if len(part.index) == 0: #If part is an empty dataframe, do not print it out
        print(f"No rows dropped for position {pos}") 
    else: #If dataframe is not empty
        parts[pos] = part #Add part to parts dictionary 
        df.drop(part.index, inplace=True) #Drops all rows from dataframe where the value in pos is equal to '-'
        print(f"{len(part.index)} rows dropped for position {pos}") #Print the amount of short sequences

print(f"{len(df.index)} rows remaining") #Print the amount of long sequences
print(f'Long sequences are in total {len(df.index)} sequences and the sequences are: {df}') #Print all long sequences


df.to_csv('Test_CDR2.csv', index = False) #Save our data in df to a csv file