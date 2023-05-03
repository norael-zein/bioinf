import pandas as pd
import sys


input_file = sys.argv[1]


df = pd.read_csv(input_file) 

filter = {'103':'-'}

for key, value in filter.items(): 
        part = df.loc[df[key] == value]
        df.drop(part.index, inplace=True)

# Determination of CDR length
counter = {'A':1,'C':1,'D':1,'E':1,'F':1,'G':1,'H':1,
           'I':1,'K':1,'L':1,'M':1,'N':1,'P':1,'Q':1,
           'R':1,'S':1,'T':1,'V':1,'W':1,'Y':1,'-':0}

print(df['35B'])

start_1 = df.columns.get_loc('30')
start_2 = df.columns.get_loc('50')
start_3 = df.columns.get_loc('95')

stop_1 = df.columns.get_loc('35B')
stop_2 = df.columns.get_loc('65')
stop_3 = df.columns.get_loc('102')

#CDR1
CDR1 = df.iloc[:,start_1:stop_1+1]
CDR1 = CDR1.replace(counter)
df['CDR1_length'] = CDR1.sum(axis=1)

# CDR2
CDR2 = df.iloc[:,start_2:stop_2+1]
CDR2 = CDR2.replace(counter)
df['CDR2_length'] = CDR2.sum(axis=1)

# CDR3
CDR3 = df.iloc[:,start_3:stop_3+1]
CDR3 = CDR3.replace(counter)
df['CDR3_length'] = CDR3.sum(axis=1)

# CDR3['CDR3_length'] = CDR3.sum(axis=1)          #sätt ihop denna o nästa rad
# df['CDR3_length'] = CDR3['CDR3_length']

df.to_csv('Test_filter.csv', index = False)