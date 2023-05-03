import pandas as pd
import sys


input_file = sys.argv[1]

raw = pd.read_csv(input_file) 
df = raw.drop(raw.columns[:13], axis=1)

pos1 = '100J' #75%

part1 = df.loc[df[pos1] == '-'] #75%
print(len(part1.index))
df.drop(df[df[pos1] == '-'].index, inplace = True) #25%
print(len(df.index))

print(part1)
print(df)