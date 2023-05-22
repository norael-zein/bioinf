import pandas as pd
import sys

input_file = sys.argv[1]
#Choice options
print("This script have multiple options of how you want the results") 
print()
type_of_seq = input("What type of sequences is in the input file? Answer for example PATENT, NGS, etc: ")
print()
print("Are you interested in filtration of the input file? Filtration will tralala.")
print("The filtered file will be used in further steps and can be provided in Filtered_<input_file-name>.csv")
filtration = input("Do you want to do filtration on the file? Answer Yes or No: ")
print()
print(f'The script can yield out the CDR regions. In CDR 1 resp 2 is filtered with a threshold of 4% gaps. ')
print (f'The sequences with a gap in that positions is considered short and the ones with a amino acid in that position - long ')
CDR1_choice = input("Do you want to yield out the CDR1, filtering the region on the threshold of 4%? Answer Yes or No: ")
CDR2_choice = input("Do you want to yield out the CDR2, filtering the region on the threshold of 4%? Answer Yes or No: ")

#Filtration 
if filtration == 'Yes': 
    raw = pd.read_csv(input_file) 
    df = raw.drop(raw.columns[:13], axis=1)

    filter = {'103':'-'}

    for key, value in filter.items(): 
        part = df.loc[df[key] == value]
        df.drop(part.index, inplace=True)

    output_name = 'Filtered_'+str(input_file)
    input_file = df.to_csv(output_name, index = False)

