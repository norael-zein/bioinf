import pandas as pd
import sys
import math

input_file = sys.argv[1]

raw = pd.read_csv(input_file)
df = raw.drop(raw.columns[[0,1,2,3,4,5,6,7,8,9,10,11,12]], axis=1)

# Creation of a frequency DataFrame
df_freq = df.apply(pd.Series.value_counts)
positions = list(df_freq.columns[:])
aminoacid = list(df_freq.index)

# Creation of a frequency dictionary from frequency DataFrame
frequencies = {'Amino_acid':['Pos'+ pos for pos in positions]}
for i, aa in enumerate(aminoacid):
    if aa == '-':
        aa = '*'
    frequencies[aa] = list(df_freq.iloc[i,:])

output_file = open('frequencies' + input_file, 'w')
for aa, freq in frequencies:
   output_file.write(aa +',')
   for f in freq:
       output_file.write(f + ',')
   output_file.write('\n')

   



#print(list(freq.iloc[0,:]))
# # Creation of a frequency dictionary from frequency DataFrame
# frequencies = {}
# for pos in positions:
#     frequencies[pos] = {"A":0, "R":0, "N":0, "D":0, "C":0,
#                         "Q":0, "E":0, "G":0, "H":0, "I":0,
#                         "L":0, "K":0, "M":0, "F":0, "P":0, 
#                         "S":0, "T":0, "W":0, "Y":0, "V":0, "*":0}
#     for aa in aminoacid:
#         count = freq[pos][aa]
#         if not math.isnan(count):
#             if aa == '-':
#                 frequencies[pos]['*'] += int(count)
#             else:
#                 frequencies[pos][aa] += int(count)

# print(frequencies)