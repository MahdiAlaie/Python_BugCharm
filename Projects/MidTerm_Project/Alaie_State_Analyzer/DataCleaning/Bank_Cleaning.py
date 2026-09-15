import pandas as pd
import os

# Read file
def ReadFile (state):
    global BankDF
    ExcelPath = f"F:\\programming\\Bootcamp\\PYBC_MidtermProject\\lib\\States_Data\\{state}"
    BankDF = pd.read_csv(os.path.join(ExcelPath,"banks.csv"))
    

