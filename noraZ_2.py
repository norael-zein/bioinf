import pandas as pd
import sys

input_file = sys.argv[1]

file = pd.read_csv(input_file) 
df = file.drop(file.columns[:13], axis=1)


length_threshold = 10 # Set the desired length threshold

long_rows = df.loc[df.apply(lambda x: x.str.len() > length_threshold).any(axis=1)]

print(long_rows)
#python noraZ_2.py test100_H.csv
