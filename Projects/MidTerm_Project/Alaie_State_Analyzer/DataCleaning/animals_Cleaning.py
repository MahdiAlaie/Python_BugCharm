import pandas as pd
import os

# Read file by enter sttate name
def ReadFile (state):
    global AnimalsDF
    ExcelPath = f"F:\\programming\\Bootcamp\\PYBC_MidtermProject\\lib\\States_Data\\{state}"
    AnimalsDF = pd.read_csv(os.path.join(ExcelPath,"animals.csv"))

# Clean data 
def Clean():
    global AnimalsDF
    AnimalsDF["Species"] = AnimalsDF["Species"].str.lower()
    AnimalsDF["Species"] = AnimalsDF["Species"].str.strip()
    return AnimalsDF

# filter viral animal
def unclean_animals():
    global unclean 
    unclean =  AnimalsDF.loc[AnimalsDF["Virus_Signature"].str.contains("VIR"),:]

