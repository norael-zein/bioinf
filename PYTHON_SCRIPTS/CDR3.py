import matplotlib.pyplot as plt
import pandas as pd
import sys


input_file = sys.argv[1]
df = pd.read_csv(input_file) 

# Determination of CDR length
counter = {'A':1,'C':1,'D':1,'E':1,'F':1,'G':1,'H':1,
           'I':1,'K':1,'L':1,'M':1,'N':1,'P':1,'Q':1,
           'R':1,'S':1,'T':1,'V':1,'W':1,'Y':1,'-':0}

start = df.columns.get_loc('95')              # Start postion CDR3
stop = df.columns.get_loc('102')              # Stop position CDR3

CDR3 = df.iloc[:,start:stop+1]
CDR3_counter = df.iloc[:,start:stop+1]
CDR3_counter = CDR3_counter.replace(counter)

CDR3['CDR3_length'] = CDR3_counter.sum(axis=1)
#CDR3_counter['CDR3_length'] = CDR3_counter.sum(axis=1)
#CDR3['CDR3_length'] = CDR3_counter['CDR3_length']
print(CDR3['CDR3_length'])
# # -------------------------------------------------
# # ------------------- PLOTTING --------------------
# # -------------------------------------------------

# min = CDR3['CDR3_length'].min()
# max = CDR3['CDR3_length'].max()

# length_range = [*range(min,max+1,1)]
# nr_sequences = []
# lengths = []
# for l in length_range:
#     part = CDR3.loc[CDR3['CDR3_length'] == l]
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
##########################################
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

# -------------------------------------------------
# ----------------- OUTPUT FILES ------------------
# -------------------------------------------------

# threshold1 = 12         
# threshold2 = 18

# # Shortest 
# short = CDR3.loc[CDR3['CDR3_length'] <= threshold1]
# short = short.drop(columns=['CDR3_length'])
# short.to_csv('CDR3_short.csv', index = False) 

# # Medium
# medium = CDR3[ (CDR3['CDR3_length'] > threshold1) & (CDR3['CDR3_length'] <= threshold2)]
# medium = medium.drop(columns=['CDR3_length'])
# medium.to_csv('CDR3_medium.csv', index = False) 

# # Long
# long = CDR3[ (CDR3['CDR3_length'] > threshold2)]
# long = long.drop(columns=['CDR3_length'])
# long.to_csv('CDR3_long.csv', index = False) 
#######################################################
# threshold1 = 12         
# threshold2 = 18

# # Shortest 
# short = df.loc[df['CDR3_length'] <= threshold1]
# short = short.drop(columns=['CDR3_length'])
# short.to_csv('CDR3_short.csv', index = False) 

# # Medium
# medium = df[ (df['CDR3_length'] > threshold1) & (df['CDR3_length'] <= threshold2)]
# medium = medium.drop(columns=['CDR3_length'])
# medium.to_csv('CDR3_medium.csv', index = False) 

# # Long
# long = df[ (df['CDR3_length'] > threshold2)]
# long = long.drop(columns=['CDR3_length'])
# long.to_csv('CDR3_long.csv', index = False) 