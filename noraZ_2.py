import pandas as pd
import sys

input_file = sys.argv[1]

raw = pd.read_csv(input_file)
df = raw.drop(raw.columns[:13], axis=1)

positions = input("Enter a comma-separated list of positions: ")
positions = positions.split(",")
positions = [pos.strip() for pos in positions]  # Enable to have space between the positions in the input
parts = {}

for pos in positions:
    part = df.loc[df[pos] == '-']
    if len(part.index) == 0:
        print(f"No rows dropped for position {pos}")
    else:
        parts[pos] = part
        df.drop(part.index, inplace=True)
        print(f"{len(part.index)} rows dropped for position {pos}")
        print(part)

print(f"{len(df.index)} rows remaining")
print(f'Long sequences: {df}')
print(f' List of short sequences: {parts}')

#Adding short sequences to a text file
with open('testoutputNoraZ.txt', 'w') as f:
    # Iterate over the dictionary items and write them to the file
    for key, value in parts.items():
        f.write(f'{key}: {value}\n')

print(parts)