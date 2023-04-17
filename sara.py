import pandas as pd
import sys

input_file = sys.argv[1]

raw = pd.read_csv(input_file)
df = raw.drop(raw.columns[[0,1,2,3,4,5,6,7,8,9,10,11,12]], axis=1)

# Creation of a frequency DataFrame
freq = df.apply(pd.Series.value_counts)
positions = list(freq.columns[:])
aminoacid = list(freq.index)

# Creation of a frequency dictionary
frequencies = {}
aminoacids = {"A":0, "R":0, "N":0, "D":0, "C":0,
              "Q":0, "E":0, "G":0, "H":0, "I":0,
              "L":0, "K":0, "M":0, "F":0, "P":0, 
              "S":0, "T":0, "W":0, "Y":0, "V":0, "*":0}
for pos in positions:
    frequencies[pos] = aminoacids
    for aa in aminoacid:
        

for pos in positions:
    for a in aminoacid:
        print(freq[pos][a])



#print(freq.loc[:, "2"])





#positions = list(df.columns[13:])
#for pos in positions:
#    frequencies[pos] = aminoacids

#bajs = df[[positions[0]]].value_counts()#print(bajs.keys())