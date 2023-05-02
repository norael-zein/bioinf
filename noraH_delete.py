import pandas as pd
import sys


input_file = sys.argv[1]

raw = pd.read_csv(input_file) 
df = raw.drop(raw.columns[:13], axis=1)
tot_seq = df.copy()

counter = {'A':1,'C':1,'D':1,'E':1,'F':1,'G':1,'H':1,
           'I':1,'K':1,'L':1,'M':1,'N':1,'P':1,'Q':1,
           'R':1,'S':1,'T':1,'V':1,'W':1,'Y':1,'-':0}


tot_seq = tot_seq.replace(counter)
tot_seq['Length'] = tot_seq.sum(axis=1)
df['Length'] = tot_seq['Length']

threshold = 100

true_seq = df.loc[df['Length']>=threshold]
df.drop(true_seq.index, inplace=True)

print(len(true_seq.index))
print(len(df.index))