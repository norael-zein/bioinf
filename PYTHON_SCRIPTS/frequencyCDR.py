import matplotlib.pyplot as plt
import pandas as pd
import sys


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

CDR = df.iloc[:,start:stop+1]
CDR = CDR.replace(counter)
CDR['CDR_length'] = CDR.sum(axis=1)          #sätt ihop denna o nästa rad
df['CDR_length'] = CDR['CDR_length']

#-----------------------------------------------------------------
# Plot number of sequences depending on CDR3 length
min = 5
min = df['CDR_length'].min()
max = df['CDR_length'].max()

length_range = [*range(min,max+1,1)]
nr_sequences = []
lengths = []
for l in length_range:
    part = df.loc[df['CDR_length'] == l]
    amount = len(part.index)
    nr_sequences.append(amount)
    lengths.append(l)

sum = sum(nr_sequences)
occurrences = [x/sum for x in nr_sequences]

plt.bar(lengths, occurrences)
plt.title('CDR2 length')
plt.xlabel('Number of amino acids')
plt.ylabel('Occurrences (%)')
plt.show()
