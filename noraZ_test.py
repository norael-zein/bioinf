import pandas as pd
import sys


input_file = sys.argv[1]

raw = pd.read_csv(input_file) 
df = raw.drop(raw.columns[:13], axis=1)
test = {}

pos1 = '100J' #75%

part1 = df.loc[df[pos1] == '-'] #75%
if len(part1.index) == 0:
    print(f"No rows dropped for position {pos1}")
print(len(part1.index))
df.drop(df[df[pos1] == '-'].index, inplace = True) #25%
print(len(df.index))
test[0] = part1

print(part1)
print(df)

pos2 = '100K' #75%

part2 = df.loc[df[pos2] == '-'] #75%
if len(part2.index) == 0:
    print(f"No rows dropped for position {pos2}")
print(len(part2.index))
df.drop(df[df[pos2] == '-'].index, inplace = True) #25%
print(len(df.index))
test[1] = part2

print(part2)
print(df)

pos3 = '100L' #75%

part3 = df.loc[df[pos3] == '-'] #75%
if len(part3.index) == 0:
    print(f"No rows dropped for position {pos3}")
print(len(part3.index))
df.drop(df[df[pos3] == '-'].index, inplace = True) #25%
print(len(df.index))
test[2] = part3
print(part3)
print(df)

pos4 = '100M' #75%

part4 = df.loc[df[pos4] == '-'] #75%
if len(part4.index) == 0:
    print(f"No rows dropped for position {pos4}")
print(len(part4.index))
df.drop(df[df[pos4] == '-'].index, inplace = True) #25%
print(len(df.index))
test[3] = part4
print(part4)
print(df)

print(test)



