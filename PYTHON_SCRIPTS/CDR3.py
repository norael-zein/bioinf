import matplotlib.pyplot as plt
import pandas as pd
import sys


input_file = sys.argv[1]

df = pd.read_csv(input_file) 
#raw = pd.read_csv(input_file) 
#df = raw.drop(raw.columns[:13], axis=1)

# Determination of CDR3 length
counter = {'A':1,'C':1,'D':1,'E':1,'F':1,'G':1,'H':1,
           'I':1,'K':1,'L':1,'M':1,'N':1,'P':1,'Q':1,
           'R':1,'S':1,'T':1,'V':1,'W':1,'Y':1,'-':0}

start = df.columns.get_loc('95')
stop = df.columns.get_loc('102')

CDR3 = df.iloc[:,start:stop+1]
CDR3 = CDR3.replace(counter)
CDR3['CDR3_length'] = CDR3.sum(axis=1)          #sätt ihop denna o nästa rad
df['CDR3_length'] = CDR3['CDR3_length']


#-----------------------------------------------------------------
# # Plot number of sequences depending on CDR3 length
# min = 5
# #min = df['CDR3_length'].min()
# max = df['CDR3_length'].max()

# length_range = [*range(min,max+1,1)]
# nr_sequences = []
# lengths = []
# for l in length_range:
#     part = df.loc[df['CDR3_length'] == l]
#     amount = len(part.index)
#     nr_sequences.append(amount)
#     lengths.append(l)

# sum = sum(nr_sequences)
# occurrences = [x/sum for x in nr_sequences]

# plt.bar(lengths, occurrences)
# plt.title('CDR3 length')
# plt.xlabel('Number of amino acids')
# plt.ylabel('Number of sequences')
# plt.show()

#-------------------------------------------------------------------
# Different output files

# # Rename the header
# pos = list(df.columns)
# pos.remove('CDR3_length')
# dic = {}
# for p in pos:
#     dic[p] = 'Pos' + p

# df.rename(columns=dic, inplace=True)

# Creation of three separate dataframes
threshold1 = 12
threshold2 = 18

short = df.loc[df['CDR3_length'] <= threshold1]
short = short.drop(columns=['CDR3_length'])
short.to_csv('CDR3_short.csv', index = False) #Save our data in df to a csv file
#short = short.apply(pd.Series.value_counts)

medium = df[ (df['CDR3_length'] > threshold1) & (df['CDR3_length'] <= threshold2)]
medium =medium.drop(columns=['CDR3_length'])
df.to_csv('CDR3_medium.csv', index = False) #Save our data in df to a csv file
#medium = medium.apply(pd.Series.value_counts)

long = df[ (df['CDR3_length'] > threshold2)]
long = long.drop(columns=['CDR3_length'])
df.to_csv('CDR3_long.csv', index = False) #Save our data in df to a csv file
#long = long.apply(pd.Series.value_counts)