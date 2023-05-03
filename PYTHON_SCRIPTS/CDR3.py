import matplotlib.pyplot as plt
import pandas as pd
import sys


input_file = sys.argv[1]

df = pd.read_csv(input_file) 

# #
# # Plotting
# #
# min = df['CDR3_length'].min()
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
# plt.ylabel('Occurrences (%)')
# plt.show()

#-------------------------------------------------------------------
# Different output files



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
