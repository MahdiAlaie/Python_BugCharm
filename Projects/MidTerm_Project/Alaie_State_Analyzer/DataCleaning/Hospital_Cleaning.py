import pandas as pd
import os
import numpy as np

# Read file
def ReadFile (state):
    global HospitalDF
    ExcelPath = f"F:\\programming\\Bootcamp\\PYBC_MidtermProject\\lib\\States_Data\\{state}"
    HospitalDF = pd.read_csv(os.path.join(ExcelPath,"hospital.csv"))

# Clean data
def Clean():
    global HospitalDF
    
    #Clean wrong body temperature
    HospitalDF.loc[HospitalDF["Body_Temperature"] > 45,"Body_Temperature"] = np.nan

    #Clean DNA Part
    HospitalDF["Patient_DNA_Sample"] = HospitalDF["Patient_DNA_Sample"].str.upper()
    
    
    return HospitalDF

#Find viral DNA
def Find_Viral():

    global ViralPatient
    global ViralDNA_Virus
    global HospitalDF

    # viral patient
    ViralPatient = HospitalDF.loc[HospitalDF["Is_Viral"]== True,:]
    
    # virus list
    ViralDNA_Virus = ViralPatient["Patient_DNA_Sample"].str.extract(r'(VIR-[0-9]{3})')
    return ViralDNA_Virus


def percetage_of_viral ():
    print(f"{HospitalDF["Is_Viral"].mean()* 100} of patients are infected!.")


