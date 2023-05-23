"""FILTRATION_FORMATION_VISUALIZATION.PY"""
import matplotlib.pyplot as plt
import pandas as pd
import sys
import numpy as np

input_file = sys.argv[1]

"""OPTIONS FOR THE USER"""
print()
print('----------------------------------------------------------')
print('--------Splitting and visualization of sequences----------')
print('----------------------------------------------------------')
print('This script filters and formats the ANARCI .csv output into several files,')
print('customized for R-scripts developed by Ella Schleimann-Jensen (2022).')
print('The content of these files are chosen by the user by answering questions') 
print('with either "Yes" or "No"')
print('Options for visualization (graphs) of the CDR length distributions is also provided.')
print('Furthermore, the script provides optional calculations correlated to the sequences protein A motifs.')
print('For more in detail information, see the user manual provided in the README file')
print()
print('--------------------------------------')
print('Type of sequences')
print('--------------------------------------')
print()
type_of_seq = input("What type of sequences does the input file contain? Answer for example PATENT, NGS, etc: ")
print()
print('--------------------------------------')
print('Filtration')
print('--------------------------------------')
print()
filtration = input("Do you wish to filter the sequences? Answer Yes or No: ")
print()
print('--------------------------------------')
print('Content of output files')
print('--------------------------------------')
print()
histogram_choice = input("Do you wish to format the sequences to the R-scripts developed by Ella Schleimann-Jensen? Answer Yes or No: ")
print()
print('--------------------------------------')
print('Output files depending on CDR length')
print('--------------------------------------')
print()
print('------------------')
print("Splitting sequences into standard length and long length (threshold set to 4% amino acids)")
print('------------------')
print()
print('----CDR1----')
CDR1_choice = input("Are you interested in splitting the sequences depending on CDR1 length? Answer Yes or No: ")
print()
print('----CDR2----')
CDR2_choice = input("Are you interested in splitting the sequences depending on CDR2 length? Answer Yes or No: ")
print()
print('------------------')
print('Splitting sequences into short length, standard length and long length depending on threshold')
print('------------------')
print()
print('----CDR3----')
CDR3_choice = input("Are you interested in splitting the sequences into three ranges depending on CDR3 length and a given threshold (next question)? Answer Yes or No: ")
print()
print('---Threshold---')
CDR3_threshold_start= input("Enter a threshold between short and standard CDR3 length: ")
CDR3_threshold_stop= input("Enter a threshold between standard and long CDR3 length: ")
print()
print('------------------')
print('Graphs of CDR1, CDR2 and CDR3 length distribution')
print('------------------')
print()
print('----CDR1----')
CDR1_graph = input("Are you interested in a graph of CDR1 length distribution? Answer Yes or No: ")
print()
print('----CDR2----')
CDR2_graph = input("Are you interested in a graph of CDR2 length distribution? Answer Yes or No: ")
print()
print('----CDR3----')
CDR3_graph = input("Are you interested in a graph of CDR3 length distribution? Answer Yes or No: ")
print()
print('----Overview----')
CDR_all = input("Are you interested in visulizing all three CDRs in one graph? Answer Yes or No: ")
print()
print('--------------------------------------')
print('Protein A motif')
print('--------------------------------------')
protein_A_choice = input("Do you wish to compute the frequency of complete protein A motifs in the sequences? Answer Yes or No: ")
print()
print('===============================================================================================')



#======================================================================================================

"""FILTRATION OF THE SEQUENCES"""
# Filters the sequences depending on the existance of an amino acid
# in postion 103. Sequences not upholding this constraint is removed.

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

#==================================================================================

"""GENERAL CODE FOR VISULAIZAITON"""
# This sections codes for all three CDRs and is used when graphing
# the CDR length distirbution. 

counter = {'A':1,'C':1,'D':1,'E':1,'F':1,'G':1,'H':1,
            'I':1,'K':1,'L':1,'M':1,'N':1,'P':1,'Q':1,
            'R':1,'S':1,'T':1,'V':1,'W':1,'Y':1,'-':0}

histogram = [input_file]

#Locating the columns within the CDRs
start_CDR1 = df.columns.get_loc('30')              # Start postion CDR1
stop_CDR1 = df.columns.get_loc('35B')              # Stop position CDR1

start_CDR2 = df.columns.get_loc('50')              # Start postion CDR1
stop_CDR2 = df.columns.get_loc('65')               # Stop position CDR1

start_CDR3 = df.columns.get_loc('95')              # Start postion CDR3
stop_CDR3 = df.columns.get_loc('102')              # Stop position CDR3


# Counts the positions and generate the sum in a new column
CDR1 = df.iloc[:,start_CDR1:stop_CDR1+1]
CDR1 = CDR1.replace(counter)
df['CDR1_length'] = CDR1.sum(axis=1)

CDR2 = df.iloc[:,start_CDR2:stop_CDR2+1]
CDR2 = CDR2.replace(counter)
df['CDR2_length'] = CDR2.sum(axis=1)

CDR3 = df.iloc[:,start_CDR3:stop_CDR3+1]
CDR3 = CDR3.replace(counter)
df['CDR3_length'] = CDR3.sum(axis=1)


#Generate the procentage of each length in the CDRs

#--CDR1--
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

#--CDR2--
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

#--CDR3--
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

#==================================================================================

"""VISUALIZAITON OF ALL THREE CDRs LENGTH DISTIRBUTION"""
# Generates a graph of all three CDRs to compare the length distibution
# in the different regions. 
 
if CDR_all == 'Yes': 
    fig, (ax1, ax2, ax3) = plt.subplots(3, figsize=(10,20), sharex=True, sharey=True)
    title_name_CDR_all = 'CDR length distribution for ' + type_of_seq + ' sequences'
    fig.suptitle(title_name_CDR_all, weight='bold', fontsize=16)

    ax1.bar(lengths_1, occurrences_1, color ='indianred', width = 0.5, label='CDR1')
    ax1.legend(loc='upper right')

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

#==================================================================================

"""VISUALIZAITON OF CDR1 LENGTH DISTRIBUTION"""
# Generates a graph of the length distribution of CDR1.

if CDR1_graph == 'Yes':
    max_value_1 = max(occurrences_1)
    print('---CDR1 length distribution---')
    print(f'The highest percentage in the CDR1 length distribution was of {max_value_1}%.')
    print()
    
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

#==================================================================================

"""VISUALIZAITON OF CDR2 LENGTH DISTRIBUTION"""
# Generates a graph of the length distribution of CDR2.

if CDR2_graph == 'Yes':
    max_value_2 = max(occurrences_2)
    print('---CDR2 length distribution---')
    print(f'The highest percentage in the CDR2 length distribution was of {max_value_2}%.')
    print()

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

#==================================================================================

"""VISUALIZAITON OF CDR3 LENGTH DISTRIBUTION"""
# Generates a graph of the length distribution of CDR3.

if CDR3_graph == 'Yes':
    max_value_3 = max(occurrences_3)
    print('---CDR3 length distribution---')
    print(f'The highest percentage in the CDR3 length distribution was of {max_value_3}%.')
    print()
    
    
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

#==================================================================================
print()

"""SPLITTING OF SEQUENCES DEPENDING ON CDR1 LENGTH"""
# Splits the sequences into two categories, one with standard length of CDR1 and one with 
# longer length of CDR1. The threshold is set to 4% amino acids. 

if CDR1_choice == 'Yes': 
    print('----- CDR1: split into sequences of standard and long length -----')
    print()
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
        print(f'The standard sequences in CDR1 are in total {len(part_1.index)} sequences') #Print the amount of short sequences
    print(f'The long sequences in CDR1 are in total {len(df_1.index)} sequences') #Print the amount of long sequences
    print()

    standard_CDR1_name = type_of_seq +'_CDR1_standard.csv'
    long_CDR1_name = type_of_seq+'_CDR1_long.csv'
    part_1.to_csv(standard_CDR1_name, index = False) #STANDARD SEQUENCES
    df_1.to_csv(long_CDR1_name, index = False) #LONG SEQUENCES
    histogram.append(standard_CDR1_name)
    histogram.append(long_CDR1_name)

#==================================================================================

"""SPLITTING OF SEQUENCES ACCORDING TO CDR2 LENGTH"""
# Splits the sequences into two categories, one with standard length of CDR2 and one with 
# long length of CDR2. The threshold is set to 4% amino acids.

if CDR2_choice == 'Yes': 
    print('----- CDR2: split into sequences of standard and long length -----')
    print()
    df_2 = pd.read_csv(input_file)
    #Input position where threshold is over 4%
    position = '52B'
    parts = {} #Short sequences added here
    part_2 = df_2.loc[df_2[position] == '-'] #Selects all the columns where values in pos is equal to '-' and put the sequences in 'part'
    if len(part_2.index) == 0: #If part is an empty dataframe, do not print it out
        print(f"No rows dropped for position {position}") 
    else: #If dataframe is not empty
        parts[position] = part_2 #Add part to parts dictionary 
        df_2.drop(part_2.index, inplace=True) #Drops all rows from dataframe where the value in pos is equal to '-'
        print(f'The standard sequences in CDR2 are in total {len(part_2.index)} sequences') #Print the amount of short sequences
    print(f'The long sequences in CDR2 are in total {len(df_2.index)} sequences') #Print the amount of long sequences
    print()
    print()

    standard_CDR2_name = type_of_seq +'_CDR1_standard.csv'
    long_CDR2_name = type_of_seq+'_CDR1_long.csv'
    part_2.to_csv(standard_CDR2_name, index = False) #STANDARD SEQUENCES
    df_2.to_csv(long_CDR2_name, index = False) #LONG SEQUENCES
    histogram.append(standard_CDR2_name)
    histogram.append(long_CDR2_name)

#==================================================================================

"""SPLITTING OF SEQUENCES INTO THREE RANGES ACCORDING TO CDR3 LENGTH"""
# Splits the sequences into three categories: short, standard and long CDR3 length. The threshold 
# between each ranges is set by the user. 

if CDR3_choice == 'Yes':

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

#==================================================================================

"""CSV-FILES FOR HISTOGRAMS"""
# Formats the output csv-files into another type of csv-file that can be used when making histogram
# (using R-script). 

if histogram_choice == 'Yes':
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

"""PROTEIN A MOTIF"""
# Calculates the percentage of sequences with a correct Protein A motif and compare
# the alternativ correct amino acid at postion 57.

if protein_A_choice == 'Yes':
    tot_seq = len(df.index)

    prot_A_dict = {'15':['G'], '17':['S'], '19':['R'], '57':['K', 'T'], '59':['Y'], '64':['K'], '65':['G'], '66':['R'], '68':['T'], '70':['S'], '81':['Q'], '82A':['N'], '82B':['S']}

    part = df.copy()
    for key, value in prot_A_dict.items(): 
            part = part.loc[df[key].isin(value)]

    correct_seq = len(part.index)

    part_K = part.loc[df['57'] == 'K']
    part.drop(part_K.index, inplace = True)

    print('------ Protein A motif ------')
    print()
    print(f'The total number of sequences where:', tot_seq)
    print(f'The number of seqeunces with all ProA positions correct:', correct_seq)
    print(f'The frequency of seqeunces with all ProA positions correct:', "{:.2f}".format((correct_seq/tot_seq)*100), '%')
    print()
    print('--- Comparision of K/T at postion 57 ---')
    print()
    print(f'The number and frequency of the correct sequences with K in position 57')
    print(f'Number of seq:', len(part_K.index))
    print(f'frequency:', "{:.2f}".format((len(part_K.index)/correct_seq)*100), '%')
    print()
    print(f'The number and frequency of the correct sequences with T in position 57:')
    print(f'Number of seq:', len(part.index))
    print(f'frequency:', "{:.2f}".format((len(part.index)/correct_seq)*100), '%')


