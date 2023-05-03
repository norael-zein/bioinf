import pandas as pd
import sys


input_file = sys.argv[1]

raw = pd.read_csv(input_file) 
df = raw.drop(raw.columns[:13], axis=1)

filter = {'103':'-'}

for key, value in filter.items(): 
        part = df.loc[df[key] == value]
        df.drop(part.index, inplace=True)

df.to_csv('Test_filter.csv', index = False)