import pandas as pd
import os
import numpy as np

# Read file
def ReadFile (state):
    global CitizensDF
    ExcelPath = f"F:\\programming\\Bootcamp\\PYBC_MidtermProject\\lib\\States_Data\\{state}"
    CitizensDF = pd.read_csv(os.path.join(ExcelPath,"citizens.csv"))


# Clean data
def Clean():
    global CitizensDF
    # clean Names columes
    CitizensDF["First_Name"] = CitizensDF["First_Name"].str.strip() 
    CitizensDF["Last_Name"] = CitizensDF["Last_Name"].str.strip() 
    CitizensDF["Last_Name"] = CitizensDF["Last_Name"].str.lower() 
    CitizensDF["First_Name"] = CitizensDF["First_Name"].str.lower() 
    CitizensDF["First_Name"] = CitizensDF["First_Name"].str.capitalize() 
    CitizensDF["Last_Name"] = CitizensDF["Last_Name"].str.capitalize() 

    # clean Phone_Number colume
    CitizensDF["Phone_Number"] = CitizensDF["Phone_Number"].str.replace(r"[^\d]","",regex=True)
    CitizensDF["Phone_Number"] = CitizensDF["Phone_Number"].str.replace(r"^(?:\+98|98|0)","",regex=True)

    # clean Email colume
    CitizensDF.loc[CitizensDF["Email"]=="Missing","Email"] = np.nan

    # clean Income colume
    CitizensDF["Monthly_Income"] = np.abs(CitizensDF["Monthly_Income"])
    
    
    return CitizensDF


