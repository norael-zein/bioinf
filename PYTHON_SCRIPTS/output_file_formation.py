import pandas as pd
import sys
import math
import time

input_file = sys.argv[1]

# Reading of the input file and dropping the first 13 columns 
# (because irrelevant for the output file)
<<<<<<< HEAD
df = pd.read_csv(input_file) 
=======
df  = pd.read_csv(input_file) 
>>>>>>> 1ccca15f9227f1d7f309f4a85bb3845bb4c93871
#df = raw.drop(raw.columns[:13], axis=1)

# Creation of a frequency DataFrame, listing the columns as positions 
# and indexes as amino acids
df_freq = df.apply(pd.Series.value_counts)
positions = list(df_freq.columns)
aminoacid = list(df_freq.index)

# Creation of a frequency dictionary from frequency DataFrame
frequencies = {'Amino_acid':['Pos'+ pos for pos in positions]}
for i, aa in enumerate(aminoacid):
    #Filling the NaN values with zeros and converts all values to integers
    frequencies[aa] = df_freq.iloc[i,:].fillna(0).astype(int)

# Creation of output file, adding the values in the right format
with open(f'frequencies_{input_file}', 'w') as output_file:
    lines = [f'{aa},' + ','.join([f if isinstance(f, str) else str(f) for f in freq]) for aa, freq in frequencies.items()]
    output_file.write('\n'.join(lines))
