import pandas as pd
import sys
import math
import time

start_time = time.time()

input_file = sys.argv[1]

raw = pd.read_csv(input_file) 
df = raw.drop(raw.columns[:13], axis=1)

# Creation of a frequency DataFrame
df_freq = df.apply(pd.Series.value_counts)
positions = list(df_freq.columns)
aminoacid = list(df_freq.index)

# Creation of a frequency dictionary from frequency DataFrame
frequencies = {'Amino_acid':['Pos'+ pos for pos in positions]}
for i, aa in enumerate(aminoacid):
    if aa == '-':
        aa = '*'
    frequencies[aa] = df_freq.iloc[i,:].astype(float).fillna(0).astype(int).tolist()  #converts the values from floats to int, filling any missing values with zeros. 

with open(f'frequencies_{input_file}', 'w') as output_file:
    lines = [f'{aa},' + ','.join([f if isinstance(f, str) else str(int(f)) for f in freq]) for aa, freq in frequencies.items()]
    output_file.write('\n'.join(lines))

end_time = time.time()
tot_time = end_time - start_time
print(f"Total time: {tot_time} seconds")