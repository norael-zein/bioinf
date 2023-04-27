import pandas as pd
import sys

input_file = sys.argv[1]

raw = pd.read_csv(input_file)
df = raw.drop(raw.columns[:13], axis=1)

#Input positions to write in the command window:
positions = input("Enter a comma-separated list of positions: ")
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
        print(part) #Print short sequence

print(f"{len(df.index)} rows remaining") #Print the amount of long sequences
print(f'Long sequences: {df}') #Print all long sequences
print(f' List of short sequences: {parts}') #Print all short sequences from the dictionary 

#Adding short sequences to a csv file BEHÖVER FIXA RÄTT FORMAT PÅ NÅGOT SÄTT
with open('testoutputNoraZ.csv', 'w') as f:
    # Iterate over the dictionary items and write them to the file
    for key, value in parts.items():
        f.write(f'{key}: {value}\n')

print(parts) #Print dictionary containing all short sequences