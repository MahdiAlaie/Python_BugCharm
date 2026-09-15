import pandas as pd
import sqlite3 as sql 
import os

database_path = "f://programming/Bootcamp//PYBC_MidtermProject//Alaie_State_Analyzer//Database"
MissionOnePath = "f:\\programming\\Bootcamp\\PYBC_MidtermProject\\Mission_one"
state = "State_04"

# connect database
conn = sql.connect(os.path.join(database_path,f"{state}_DataBase.db"))
cursor = conn.cursor()

# read data
Hospital = pd.read_sql("SELECT * FROM Hospital",conn)
Citizens = pd.read_sql("SELECT * FROM Citizens",conn)

# merge data
MergedDF = pd.merge(Hospital,Citizens,left_on="Citizen_ID" , right_on="Citizen_ID",how= "inner")

#filter data
Viral_Patient = MergedDF.loc[MergedDF["Is_Viral"]==True,["Citizen_ID","First_Name","Last_Name","Address","Phone_Number"]]
Viral_Patient = Viral_Patient.reset_index(drop=True)

# extarct data
Viral_Patient.to_csv(os.path.join(MissionOnePath,f"{state}_Viral_Patients_Address.csv"))

