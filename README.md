# User manual to the bioinformatic analysis about camelid sdAbs sequences
***

The script "Splitting_Visualization.py" plays a crucial role in the bioinformatic analysis presented in our report titled "Camelid sdAbs." It offers users various options to choose from based on their specific interests. The script operates by taking a fasta file as input, which is generated through the annotation process in ANARCI (refer to the respective manual for guidance on annotating sequences). The output of the annotation is then formatted and split in different ways using this script.

To run the script, simply enter the following command in the terminal:

python Splitting_Visualization.py <input_file.fasta>

Once the script is initiated, users will be prompted with multiple questions that allow them to filter and select the desired results. By providing responses to these questions, users can tailor the output to their specific areas of interest. To ensure informed decision-making when running the script, the following explanation outlines the purpose of each question posed by the script.


##Type of sequences
--------------------------------------
"What type of sequences contains the input file? Answer for example PATENT, NGS, etc: "

The user will be prompted to specify the type of sequences contained in the input file. This allows for proper labeling of output files and graphs, particularly when making comparisons between different types of sequences analyzed in the report. If the type of sequence is unknown or not applicable, the field can be left blank by entering a space (" ").


##Filtration
--------------------------------------
"Are you interested in filtering the sequences? Answer Yes or No: "

During the running of the script, the user will be given the option to filter the sequences based on specific criteria. In this case, the sequences will be filtered based on the requirements of the presence of an amino acid at position 103 and the inclusion of the last framework region (FR4). Sequences that do not meet these criteria, can indicate that they are too short and potentially unreliable for analysis. The script will prompt the user with the question of whether they would like to remove such sequences that do not fulfill the requirements.

--------------------------------------
##CDR length distirbution - visualized in graphs
-------------------------------------- 

"Are you interested in visulizing all three CDRs in one graph? Answer Yes or No: "

The script provides the option to visualize the length distribution of all three complementarity-determining regions (CDRs) of the sequences in a single graph. By answering "Yes" to the question, the script will generate a graph that provides an overview of the CDR lengths and allows for comparisons and observations of variations and conservations in the length distribution among the CDRs.

----CDR1----

"Are you interested in a graph of CDR1 length distribution? Answer Yes or No: "

If the user answers "Yes" to the question regarding a graph of CDR1 length distribution, the script will generate a graph displaying the distribution of CDR1 lengths in the sequences. The script will also provide the percentage of the highest peak in the graph, which corresponds to the most common CDR1 lengths in the sequences. 

----CDR2----

"Are you interested in a graph of CDR2 length distribution? Answer Yes or No: "

If the user answers "Yes" to the question regarding a graph of CDR2 length distribution, the script will generate a graph displaying the distribution of CDR2 lengths in the sequences. The script will also provide the percentage of the highest peak in the graph, which corresponds to the most common CDR2 lengths in the sequences. 

----CDR3----

"Are you interested in a graph of CDR3 length distribution? Answer Yes or No: "

If the user answers "Yes" to the question regarding a graph of CDR1 length distribution, the script will generate a graph displaying the distribution of CDR1 lengths in the sequences. The script will also provide the percentage of the highest peak in the graph, which corresponds to the most common CDR1 lengths in the sequences. 


##Splitting of the sequences
--------------------------------------


###Splitting sequences into standard length and long length (threshold set to 4% amino acids)
-----

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



