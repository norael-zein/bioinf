import matplotlib.pyplot as plt
import pandas as pd
import sys
import numpy as np


input_file = sys.argv[1]

# df = pd.read_csv(input_file) 
raw = pd.read_csv(input_file) 
df = raw.drop(raw.columns[:13], axis=1) #KOLLA OM DENNA VERKLIGEN BEHÖVS DÅ HEADERN HAR TAGITS BORT

# Determination of CDR length
counter = {'A':1,'C':1,'D':1,'E':1,'F':1,'G':1,'H':1,
           'I':1,'K':1,'L':1,'M':1,'N':1,'P':1,'Q':1,
           'R':1,'S':1,'T':1,'V':1,'W':1,'Y':1,'-':0}

start = df.columns.get_loc(input("Enter a comma-separated list of positions: ") )
stop = df.columns.get_loc(input("Enter a comma-separated list of positions: ") )

#CDR1: 30-35B
#CDR2: 50-65
#CDR3_ 95-102

CDR = df.iloc[:,start:stop+1]
CDR = CDR.replace(counter)
CDR['CDR_length'] = CDR.sum(axis=1)          #sätt ihop denna o nästa rad
df['CDR_length'] = CDR['CDR_length']

#-----------------------------------------------------------------
# Plot number of sequences depending on CDR3 length

min = df['CDR_length'].min()
max_ = df['CDR_length'].max()


length_range = [*range(min,max_+1,1)]
nr_sequences = []
lengths = []
for l in length_range:
    part = df.loc[df['CDR_length'] == l]
    amount = len(part.index)
    nr_sequences.append(amount)
    lengths.append(l)


sum = sum(nr_sequences)
occurrences = [(x/sum)*100 for x in nr_sequences]
max_value = max(occurrences)
print(max_value)

fig = plt.figure (figsize = (10,5))
plt.bar(lengths, occurrences, color = 'firebrick', width = 0.5)
plt.xticks(np.arange(0, 31, step=1))
plt.xlim([0, 30])
plt.title('CDR3 length distribution', weight='bold', fontsize = 14)
plt.xlabel('CDR3 length (aa)')
plt.ylabel('Occurrences (%)')
plt.show()

#CDR1: width= 0.5, range(0,15)
#CDR2: width=0.5, range(11,26)
#CDR3: width= 0.5, range(0,30)

