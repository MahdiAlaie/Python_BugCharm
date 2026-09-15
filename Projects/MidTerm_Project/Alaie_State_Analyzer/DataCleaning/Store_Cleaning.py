import pandas as pd
import os
import numpy as np

# Read file
def ReadFile (state):
    global StoreDF
    ExcelPath = f"F:\\programming\\Bootcamp\\PYBC_MidtermProject\\lib\\States_Data\\{state}"
    StoreDF = pd.read_csv(os.path.join(ExcelPath,"stores_purchases.csv"))

# Clean data
def Clean():

    global StoreDF

    # Clean dublicate rows    
    CurruntRows = StoreDF.index.stop
    StoreDF = StoreDF.drop_duplicates()
    AfterCleanRows = StoreDF.index.stop
    
    # show changes
    print(f"{CurruntRows-AfterCleanRows} Rows has been deleted")
    
    return StoreDF
