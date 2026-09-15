import pandas as pd
import os
import sqlite3 as sql
import sys
sys.path.append("f://programming/Bootcamp//PYBC_MidtermProject")
from Alaie_State_Analyzer import Vrius_Analyzer_Class as virus_Analyzer

database_path = "f://programming/Bootcamp//PYBC_MidtermProject//Alaie_State_Analyzer//Database"
mission_one_path ="F:\programming\Bootcamp\PYBC_MidtermProject\Mission_one"
state ="State_04"

# connect database
conn = sql.connect(os.path.join(database_path,f"{state}_DataBase.db"))

# read data
HospitalDF = pd.read_sql("SELECT * FROM Hospital",conn)
CitizenDF = pd.read_sql("SELECT * FROM Citizens",conn)

# make object
Virus_Analyze = virus_Analyzer.Virus_Analyzer(HospitalDF)

# find first patient
find_patient_zero = Virus_Analyze.find_patient_zero()

# convert to a one row data
patient_zero = find_patient_zero.to_frame().T

# merge data
MergeDF = pd.merge(patient_zero,CitizenDF,left_on="Citizen_ID",right_on="Citizen_ID",how="inner") 

# filter data
MergeDF = MergeDF[["Citizen_ID","First_Name","Last_Name","Phone_Number","Address","Admission","Symptoms"]]

# extarct data
MergeDF.to_csv(os.path.join(mission_one_path,f"{state}_Patient_Zero.csv"))
