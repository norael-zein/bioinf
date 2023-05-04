import pandas as pd
import sys


input_file = sys.argv[1]

df = pd.read_csv(input_file) 
#df = raw.drop(raw.columns[:13], axis=1)

tot_seq = len(df.index)

prot_A_dict = {'15':['G'], '17':['S'], '19':['R'], '57':['K', 'T'], '59':['Y'], '64':['K'], '65':['G'], '66':['R'], '68':['T'], '70':['S'], '81':['Q'], '82A':['N'], '82B':['S']}

part = df.copy()
for key, value in prot_A_dict.items(): 
        part = part.loc[df[key].isin(value)]

correct_seq = len(part.index)

#The dataframe everything but those with correct ProA positions
#df.drop(part.index, inplace = True)

part_K = part.loc[df['57'] == 'K']
part.drop(part_K.index, inplace = True)

print(f'The total number of sequences where:', tot_seq)
print(f'The number of seqeunces with all ProA positions correct:', correct_seq)
print(f'The procent of seqeunces with all ProA positions correct:', "{:.2f}".format((correct_seq/tot_seq)*100), '%')
print()
print(f'The number and procent of the correct sequences with K in position 57')
print(f'Number of seq:', len(part_K.index))
print(f'Procent:', "{:.2f}".format((len(part_K.index)/correct_seq)*100), '%')
print(f'The number and procent of the correct sequences with T in position 57:')
print(f'Number of seq:', len(part.index))
print(f'Procent:', "{:.2f}".format((len(part.index)/correct_seq)*100), '%')