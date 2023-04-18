#Use python [script name] [file name] in the terminal to get the output of the script
import pandas as pd
import sys

#Create the dataframe 
input_file = sys.argv[1]
raw_df = pd.read_csv(input_file)
df = raw_df.drop(raw_df.columns[[0,1,2,3,4,5,6,7,8,9,10,11,12]], axis=1)

#Calculate the frequency 
freq = df.apply(pd.Series.value_counts)
positions = list(freq.columns[:])
aminoacid = list(freq.index)

for pos in positions:
    for a in aminoacid:
        print(freq[pos][a])



#print(freq.loc[:, "2"])



frequencies = {}
aminoacids = {"A":0, "R":0, "N":0, "D":0, "C":0,
              "Q":0, "E":0, "G":0, "H":0, "I":0,
              "L":0, "K":0, "M":0, "F":0, "P":0, 
              "S":0, "T":0, "W":0, "Y":0, "V":0, "*":0}

#positions = list(df.columns[13:])
#for pos in positions:
#    frequencies[pos] = aminoacids

#bajs = df[[positions[0]]].value_counts()#print(bajs.keys())


