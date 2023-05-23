# User manual to the bioinformatic analysis about camelid sdAbs sequences
***

The script "Splitting_Visualization.py" plays a crucial role in the bioinformatic analysis presented in our report titled "Camelid sdAbs." It offers users various options to choose from based on their specific interests. The script operates by taking a fasta file as input, which is generated through the annotation process in ANARCI (refer to the respective manual for guidance on annotating sequences). The output of the annotation is then formatted and split in different ways using this script.

To run the script, simply enter the following command in the terminal:

python Splitting_Visualization.py <input_file.fasta>

Once the script is initiated, users will be prompted with multiple questions that allow them to filter and select the desired results. By providing responses to these questions, users can tailor the output to their specific areas of interest. To ensure informed decision-making when running the script, the following explanation outlines the purpose of each question posed by the script.


Type of sequences
--------------------------------------
"What type of sequences contains the input file? Answer for example PATENT, NGS, etc: "

The user will be asked which type of sequences is contained in the input file. This refers to if the file includes NGS sequences or patent sequences for example (which is the two types of sequences analyised in this report). The question is simple to be able to label the output files and graphs with the right type of sequence if comparision is done. It can be left with a " " if the type of sequence is unknown. 

--------------------------------------
Filtration
--------------------------------------
"Are you interested in filtering the sequences? Answer Yes or No: "

Filtering the sequences means that the sequences needs to have an amino acid at postion 103 and also needs to contain the last framework region (FR4). If the filters does not fulfill these requirements, it is probably a sequences that is to short and might not be realiable in the analysis. The script will therefore ask the user if they want to remove these sequences that do not fulfill the requirments. 


--------------------------------------
CDR length distirbution - visualized in graphs
--------------------------------------
"Are you interested in visulizing all three CDRs in one graph? Answer Yes or No: "


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
print()
print('--------------------------------------')
print('Splitting of the sequences')
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
print('--------------------------------------')
print('Histograms')
print('--------------------------------------')
print()
histogram_choice = input("Are you interested in doing histograms of the data? Answer Yes or No: ")
print()
print('--------------------------------------')
print('Protein A motif')
print('--------------------------------------')
protein_A_choice = input("Are you interested in knowing the statistics of Protein A motif in the sequences? Answer Yes or No: ")
print()
print('===============================================================================================')



