import matplotlib.pyplot as plt
import pandas as pd
import sys
import numpy as np


input_file = sys.argv[1]
df = pd.read_csv(input_file) 

# -------------------------------------------------
# --------- DETERMINATION OF CDR3 LENGTH ----------
# -------------------------------------------------
counter = {'A':1,'C':1,'D':1,'E':1,'F':1,'G':1,'H':1,
           'I':1,'K':1,'L':1,'M':1,'N':1,'P':1,'Q':1,
           'R':1,'S':1,'T':1,'V':1,'W':1,'Y':1,'-':0}

start_1 = df.columns.get_loc('30')              # Start postion CDR1
stop_1 = df.columns.get_loc('35B')              # Stop position CDR1

start_2 = df.columns.get_loc('50')              # Start postion CDR1
stop_2 = df.columns.get_loc('65')               # Stop position CDR1

start_3 = df.columns.get_loc('95')              # Start postion CDR3
stop_3 = df.columns.get_loc('102')              # Stop position CDR3

# CDR1
CDR1 = df.iloc[:,start_1:stop_1+1]
CDR1 = CDR1.replace(counter)
df['CDR1_length'] = CDR1.sum(axis=1)

# CDR2
CDR2 = df.iloc[:,start_2:stop_2+1]
CDR2 = CDR2.replace(counter)
df['CDR2_length'] = CDR2.sum(axis=1)

CDR3 = df.iloc[:,start_3:stop_3+1]
CDR3 = CDR3.replace(counter)
df['CDR3_length'] = CDR3.sum(axis=1)

# -------------------------------------------------
# ------------------- PLOTTING --------------------
# -------------------------------------------------

# CDR1
min_1 = df['CDR1_length'].min()
max_1 = df['CDR1_length'].max()

length_range_1 = [*range(min_1,max_1+1,1)]
nr_sequences_1 = []
lengths_1 = []
for l in length_range_1:
    part = df.loc[df['CDR1_length'] == l]
    amount = len(part.index)
    nr_sequences_1.append(amount)
    lengths_1.append(l)

sum_1 = sum(nr_sequences_1)
occurrences_1 = [(x/sum_1)*100 for x in nr_sequences_1]

# CDR2
min_2 = df['CDR2_length'].min()
max_2 = df['CDR2_length'].max()

length_range_2 = [*range(min_2,max_2+1,1)]
nr_sequences_2 = []
lengths_2 = []
for l in length_range_2:
    part = df.loc[df['CDR2_length'] == l]
    amount = len(part.index)
    nr_sequences_2.append(amount)
    lengths_2.append(l)

sum_2 = sum(nr_sequences_2)
occurrences_2 = [(x/sum_2)*100 for x in nr_sequences_2]

# CDR3
min_3 = df['CDR3_length'].min()
max_3 = df['CDR3_length'].max()

length_range_3 = [*range(min_3,max_3+1,1)]
nr_sequences_3 = []
lengths_3 = []
for l in length_range_3:
    part = df.loc[df['CDR3_length'] == l]
    amount = len(part.index)
    nr_sequences_3.append(amount)
    lengths_3.append(l)

sum_3 = sum(nr_sequences_3)
occurrences_3 = [(x/sum_3)*100 for x in nr_sequences_3]

###########################################################
fig, (ax1, ax2, ax3) = plt.subplots(3, figsize=(10,20), sharex=True, sharey=True)
fig.suptitle('CDR length distribution', weight='bold', fontsize=16)

ax1.bar(lengths_1, occurrences_1, color ='indianred', width = 0.5, label='CDR1')
ax1.legend(loc='upper right')
#ax1.title.set_text('CDR length distribution')

ax2.bar(lengths_2, occurrences_2, color ='firebrick', width = 0.5, label='CDR2')
ax2.set_ylabel('Occurrences (%)')
ax2.legend(loc='upper right')

ax3.bar(lengths_3, occurrences_3, color ='darkred', width = 0.5, label='CDR3')
ax3.set_xlabel('CDR length (aa)')
ax3.legend(loc='upper right')

plt.xticks(np.arange(0, 31, step=1))
plt.xlim([0, 30])
plt.ylim([0,100])
plt.show()