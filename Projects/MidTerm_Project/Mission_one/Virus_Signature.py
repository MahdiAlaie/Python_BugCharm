import pandas as pd
import sys
import os
from matplotlib import pyplot as plt
sys.path.append("f:\programming\Bootcamp\PYBC_MidtermProject")
from Alaie_State_Analyzer.DataCleaning import Hospital_Cleaning as hospital
from Alaie_State_Analyzer.DataCleaning import animals_Cleaning as animal

MissionOnePath = "f:\\programming\\Bootcamp\\PYBC_MidtermProject\\Mission_one"
state = "State_04"

# read and clean hospital data
hospital.ReadFile(state)
hospital.Clean()
hospital.Find_Viral()
ViralDNA_Virus = hospital.ViralDNA_Virus
ViralPatient = hospital.ViralPatient

# read and clean animals data
animal.ReadFile(state)
animal.Clean()
animal.unclean_animals()
AnimalDF = animal.unclean

# add virus signature colume to hospital data
ViralPatient["Virus_Signature"] = ViralDNA_Virus

# merge data
MergeDF = pd.merge(AnimalDF,ViralPatient,left_on="Virus_Signature", right_on="Virus_Signature",how="inner")

# filter data
MergeDF = MergeDF[["Animal_ID","Species","Virus_Signature","Citizen_ID","Patient_DNA_Sample","Symptoms"]]

# extarct data
MergeDF.to_csv(os.path.join(MissionOnePath,f"{state}_Virus_Signature.csv"))

# calculate symptom count
SymptomsCount = MergeDF["Symptoms"].value_counts()

# calclate species count
SpeciesCount = MergeDF["Species"].value_counts()

# draw bar chart on species
plt.figure()
plt.bar(SpeciesCount.index,SpeciesCount.values,color="teal",width=0.6)
plt.title("Species Counts",color="m")
plt.xlabel("Species Names",color = "Blue")
plt.ylabel("Counts",color= "Blue")
plt.xticks(SpeciesCount.index)
plt.savefig(os.path.join(MissionOnePath,f"{state}_Species_Chart.png"),dpi = 300,bbox_inches='tight')

#draw bar chart on symptoms
plt.figure()
plt.barh(SymptomsCount.index,SymptomsCount.values,color="teal")
plt.title("Symptoms Counts",color="m")
plt.ylabel("Symptoms",color = "Blue")
plt.xlabel("Counts",color= "Blue")
plt.yticks(SymptomsCount.index)
plt.savefig(os.path.join(MissionOnePath,f"{state}_Symptoms_Chart.png"),dpi = 300,bbox_inches='tight')
