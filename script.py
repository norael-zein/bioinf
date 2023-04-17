import pandas as pd
import sys

input_file = sys.argv[1]
df = pd.read_csv(input_file)

frequencies = {}
aminoacids = {"A":0, "R":0, "N":0, "D":0, "C":0,
              "Q":0, "E":0, "G":0, "H":0, "I":0,
              "L":0, "K":0, "M":0, "F":0, "P":0, 
              "S":0, "T":0, "W":0, "Y":0, "V":0, "*":0}

positions = list(df.columns[13:])
for pos in positions:
    frequencies[pos] = aminoacids


