import pandas as pd

class Virus_Analyzer :
    def __init__(self,dataframe):
        self.df = dataframe
    
    # find first patient
    def find_patient_zero(self):
        self.df["Admission"] = pd.to_datetime(self.df["Admission"])

        # first patient index
        first_patient_index = self.df.loc[self.df["Is_Viral"]==True,:]
        first_patient_index = self.df["Admission"].idxmin()

        # find data
        patient_zero = self.df.loc[first_patient_index]

        return patient_zero

