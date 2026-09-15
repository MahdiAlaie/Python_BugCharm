import pandas as pd
import os
import numpy as np

# Read file
def ReadFile (state):
    global TrafficDF
    ExcelPath = f"F:\\programming\\Bootcamp\\PYBC_MidtermProject\\lib\\States_Data\\{state}"
    TrafficDF = pd.read_csv(os.path.join(ExcelPath,"police_traffic.csv"))

# Clean data
def Clean():

    global TrafficDF
    
    # clean duplicate rows
    CurruntRows = TrafficDF.index.stop
    TrafficDF = TrafficDF.drop_duplicates()
    AfterCleanRows = TrafficDF.index.stop
    
    # show changes
    print(f"{CurruntRows-AfterCleanRows} Rows has been deleted")

    # clean address
    TrafficDF["Camera_Address"] = TrafficDF["Camera_Address"].str.replace(r"St.","Street")

