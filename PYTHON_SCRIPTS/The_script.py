import matplotlib.pyplot as plt
import pandas as pd
import sys
import numpy as np

input_file = sys.argv[1]
#REWRITE THE QUESTIONS

#Choice options
print("This script have multiple options of how you want the results") 
print()
type_of_seq = input("What type of sequences is in the input file? Answer for example PATENT, NGS, etc: ")
print()
print("Are you interested in filtration of the input file? Filtration will tralala.")
print("The filtered file will be used in further steps and can be provided in Filtered_<input_file-name>.csv")
print()
filtration = input("Do you want to do filtration on the file? Answer Yes or No: ")
print()
CDR_all = input("Do you want to visulize all three CDRs in one graph? Answer Yes or No: ")
print()
print(f'The CDR1, CDR2 and CRD3 can be visulaized its length distribution in graphs: ')
CDR1_graph = input("Do you want a graph of CDR1 length distribution? Answer Yes or No: ")
CDR2_graph = input("Do you want a graph of CDR2 length distribution? Answer Yes or No: ")
CDR3_graph = input("Do you want a graph of CDR3 length distribution? Answer Yes or No: ")
print()
print(f'The script can yield out the CDR regions. In CDR 1 resp 2 is filtered with a threshold of 4% gaps. ')
print (f'The sequences with a gap in that positions is considered short and the ones with a amino acid in that position - long ')
print()
CDR1_choice = input("Do you want to yield out the CDR1, filtering the region on the threshold of 4%? Answer Yes or No: ")
CDR2_choice = input("Do you want to yield out the CDR2, filtering the region on the threshold of 4%? Answer Yes or No: ")
print()
CDR3_choice = input("Do you want to yield out CDR3 in three ranges (short, standard and long), and do that thing? Answer Yes or No: ")
CDR3_threshold_start= input("Do you want to enter a start threshold? Enter a threshold length or press enter: ")
CDR3_threshold_stop= input("Do you want to enter a stop threshold? Enter a threshold length or press enter: ")
print()
histogram_choice = input("Do you want to do histograms of the data? Answer Yes or No: ")
print()
protein_A_choice = input("Are you interested in knowing the statistics of Protein A motif in the sequences? Answer Yes or No: ")

#Filtration 
if filtration == 'Yes': 
    raw = pd.read_csv(input_file) 
    df = raw.drop(raw.columns[:13], axis=1)

    filter = {'103':'-'}

    for key, value in filter.items(): 
        part = df.loc[df[key] == value]
        df.drop(part.index, inplace=True)

    input_file = 'Filtered_'+str(input_file)
    df.to_csv(input_file, index = False)

else: 
    df = pd.read_csv(input_file) 

#__________________________
#GENERALA FOR GRAPHS

counter = {'A':1,'C':1,'D':1,'E':1,'F':1,'G':1,'H':1,
            'I':1,'K':1,'L':1,'M':1,'N':1,'P':1,'Q':1,
            'R':1,'S':1,'T':1,'V':1,'W':1,'Y':1,'-':0}

start_CDR1 = df.columns.get_loc('30')              # Start postion CDR1
stop_CDR1 = df.columns.get_loc('35B')              # Stop position CDR1

start_CDR2 = df.columns.get_loc('50')              # Start postion CDR1
stop_CDR2 = df.columns.get_loc('65')               # Stop position CDR1

start_CDR3 = df.columns.get_loc('95')              # Start postion CDR3
stop_CDR3 = df.columns.get_loc('102')              # Stop position CDR3

# CDR1
CDR1 = df.iloc[:,start_CDR1:stop_CDR1+1]
CDR1 = CDR1.replace(counter)
df['CDR1_length'] = CDR1.sum(axis=1)

# CDR2
CDR2 = df.iloc[:,start_CDR2:stop_CDR2+1]
CDR2 = CDR2.replace(counter)
df['CDR2_length'] = CDR2.sum(axis=1)

CDR3 = df.iloc[:,start_CDR3:stop_CDR3+1]
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

#________________________
#CDR ALL - graph
if CDR_all == 'Yes': 
    
    ###########################################################
    fig, (ax1, ax2, ax3) = plt.subplots(3, figsize=(10,20), sharex=True, sharey=True)
    title_name_CDR_all = 'CDR length distribution for ' + type_of_seq + ' sequences'
    fig.suptitle(title_name_CDR_all, weight='bold', fontsize=16)

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
    figure_name_CDR_all = type_of_seq + '_CDR_length_distribution.png'
    plt.savefig(figure_name_CDR_all)


#CDR1, 2, 3 - graphs
#CDR1: width= 0.5, range(0,15)
#CDR2: width=0.5, range(11,26)
#CDR3: width= 0.5, range(0,30)

if CDR1_graph == 'Yes':
    max_value_1 = max(occurrences_1)
    print(f'The highest percentage in the CDR1 length distribution was of {max_value_1}%.')

    fig = plt.figure (figsize = (4,5))
    plt.bar(lengths_1, occurrences_1, color = 'firebrick', width = 0.5)
    plt.xticks(np.arange(0, 31, step=1))
    plt.xlim([0, 15])
    title_name_CDR1 = 'CDR1 length distribution for ' + type_of_seq + ' sequences'
    plt.title(title_name_CDR1, weight='bold', fontsize = 10)
    plt.xlabel('CDR1 length (aa)')
    plt.ylabel('Occurrences (%)')
    figure_name_CDR1 = type_of_seq + "_CDR1_length distribution.png"
    plt.savefig(figure_name_CDR1)

if CDR2_graph == 'Yes':
    max_value_2 = max(occurrences_2)
    print(f'The highest percentage in the CDR2 length distribution was of {max_value_2}%.')

    fig = plt.figure (figsize = (4,5))
    plt.bar(lengths_2, occurrences_2, color = 'firebrick', width = 0.5)
    plt.xticks(np.arange(0, 31, step=1))
    plt.xlim([11, 26])
    title_name_CDR2 = 'CDR2 length distribution for ' + type_of_seq + ' sequences'
    plt.title(title_name_CDR2, weight='bold', fontsize = 10)
    plt.xlabel('CDR2 length (aa)')
    plt.ylabel('Occurrences (%)')
    figure_name_CDR2 = type_of_seq + "_CDR2_length distribution.png"
    plt.savefig(figure_name_CDR2)

if CDR3_graph == 'Yes':
    max_value_3 = max(occurrences_3)
    print(f'The highest percentage in the CDR3 length distribution was of {max_value_3}%.')

    fig = plt.figure (figsize = (10,5))
    plt.bar(lengths_3, occurrences_3, color = 'firebrick', width = 0.5)
    plt.xticks(np.arange(0, 31, step=1))
    plt.xlim([0, 30])
    title_name_CDR3 = 'CDR3 length distribution for ' + type_of_seq + ' sequences'
    plt.title(title_name_CDR3, weight='bold', fontsize = 14)
    plt.xlabel('CDR3 length (aa)')
    plt.ylabel('Occurrences (%)')
    figure_name_CDR3 = type_of_seq + "_CDR3_length distribution.png"
    plt.savefig(figure_name_CDR3)


 #______________________________________________________________________
#HISTOGRAMS
histogram = [input_file]
#CDR1 och CDR2

if CDR1_choice == 'Yes': 
    df_1 = pd.read_csv(input_file)
    #Input position where threshold is over 4%
    position = '35A'
    parts = {} #Short sequences added here
    part_1 = df_1.loc[df_1[position] == '-'] #Selects all the columns where values in pos is equal to '-' and put the sequences in 'part'
    if len(part_1.index) == 0: #If part is an empty dataframe, do not print it out
        print(f"No rows dropped for position {position}") 
    else: #If dataframe is not empty
        parts[position] = part_1 #Add part to parts dictionary 
        df_1.drop(part_1.index, inplace=True) #Drops all rows from dataframe where the value in pos is equal to '-'
        print(f'The short sequences in CDR1 are in total {len(part_1.index)} sequences') #Print the amount of short sequences

    print(f'The long sequences in CDR1 are in total {len(df_1.index)} sequences') #Print the amount of long sequences
    short_CDR1_name = type_of_seq +'_CDR1_short.csv'
    long_CDR1_name = type_of_seq+'_CDR1_long.csv'
    part_1.to_csv(short_CDR1_name, index = False) #SHORT SEQUENCES
    df_1.to_csv(long_CDR1_name, index = False) #LONG SEQUENCES
    histogram.append(short_CDR1_name)
    histogram.append(long_CDR1_name)

if CDR2_choice == 'Yes': 
    df_2 = pd.read_csv(input_file)
    #Input position where threshold is over 4%
    position = '52B'
    parts = {} #Short sequences added here
    part_2 = df_2.loc[df_2[position] == '-'] #Selects all the columns where values in pos is equal to '-' and put the sequences in 'part'
    if len(part_2.index) == 0: #If part is an empty dataframe, do not print it out
        print(f"No rows dropped for position {position}") 
    else: #If dataframe is not empty
        parts[position] = part_2 #Add part to parts dictionary 
        df.drop(part_2.index, inplace=True) #Drops all rows from dataframe where the value in pos is equal to '-'
        print(f'The short sequences in CDR2 are in total {len(part_2.index)} sequences') #Print the amount of short sequences
    print(f'The long sequences in CDR2 are in total {len(df_2.index)} sequences') #Print the amount of long sequences

    short_CDR2_name = type_of_seq +'_CDR1_short.csv'
    long_CDR2_name = type_of_seq+'_CDR1_long.csv'
    part_2.to_csv(short_CDR2_name, index = False) #SHORT SEQUENCES
    df_2.to_csv(long_CDR2_name, index = False) #LONG SEQUENCES
    histogram.append(short_CDR2_name)
    histogram.append(long_CDR2_name)

#CDR3 - ranges

if CDR3_choice == 'Yes':
         
# -------------------------------------------------
# ----------------- OUTPUT FILES ------------------
# -------------------------------------------------

    # Shortest 
    short = df.loc[df['CDR3_length'] < int(CDR3_threshold_start)]
    short = short.drop(columns=['CDR3_length'])
    short_CDR3_name = type_of_seq + '_CDR3_short.csv'
    short.to_csv(short_CDR3_name, index = False) 
    histogram.append(short_CDR3_name)

    # Standard
    standard = df[ (df['CDR3_length'] >= int(CDR3_threshold_start)) & (df['CDR3_length'] <= int(CDR3_threshold_stop))]
    standard = standard.drop(columns=['CDR3_length'])
    standard_CDR3_name = type_of_seq + '_CDR3_standard.csv'
    standard.to_csv(standard_CDR3_name, index = False) 
    histogram.append(standard_CDR3_name)

    # Long
    long = df[ (df['CDR3_length'] > int(CDR3_threshold_stop))]
    long = long.drop(columns=['CDR3_length'])
    long_CDR3_name = type_of_seq + '_CDR3_long.csv'
    long.to_csv(long_CDR3_name, index = False) 
    histogram.append(long_CDR3_name)

if histogram_choice == 'Yes':
    
    # Reading of the input file and dropping the first 13 columns 
    # (because irrelevant for the output file)
    for file in histogram: 
        df  = pd.read_csv(file) 

        # Creation of a frequency DataFrame, listing the columns as positions 
        # and indexes as amino acids
        df_freq = df.apply(pd.Series.value_counts)
        positions = list(df_freq.columns)
        aminoacid = list(df_freq.index)
        
        # Creation of a frequency dictionary from frequency DataFrame
        frequencies = {'Amino_acid':['Pos'+ pos for pos in positions]}
        for i, aa in enumerate(aminoacid):
            #Filling the NaN values with zeros and converts all values to integers
            frequencies[aa] = df_freq.iloc[i,:].fillna(0).astype(int)


        name = file.strip('.csv')
        # Creation of output file, adding the values in the right format
        with open(f'frequencies_{name}_aa_occurrences.csv', 'w') as output_file:
            lines = [f'{aa},' + ','.join([f if isinstance(f, str) else str(f) for f in freq]) for aa, freq in frequencies.items()]
            output_file.write('\n'.join(lines))

if protein_A_choice == 'Yes':
    
    tot_seq = len(df.index)

    prot_A_dict = {'15':['G'], '17':['S'], '19':['R'], '57':['K', 'T'], '59':['Y'], '64':['K'], '65':['G'], '66':['R'], '68':['T'], '70':['S'], '81':['Q'], '82A':['N'], '82B':['S']}

    part = df.copy()
    for key, value in prot_A_dict.items(): 
            part = part.loc[df[key].isin(value)]

    correct_seq = len(part.index)

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


