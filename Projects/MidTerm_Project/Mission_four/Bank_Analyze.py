import pandas as pd
import sqlite3 as sql
import os
import sys
sys.path.append("F:\programming\Bootcamp\PYBC_MidtermProject")
from Alaie_State_Analyzer import Bank_analyzer_Class as analyzer

database_path = "f://programming/Bootcamp//PYBC_MidtermProject//Alaie_State_Analyzer//Database"
mission_four_path ="F:\programming\Bootcamp\PYBC_MidtermProject\Mission_four"
state = "State_13"

# connect to data base
conn = sql.connect(os.path.join(database_path,"State_13_DataBase.db"))

# read data from database
CitizenDF = pd.read_sql("SELECT * FROM Citizens",conn)
BanksDF = pd.read_sql("SELECT * FROM Banks",conn)

# merge data
MergeDF = pd.merge(CitizenDF,BanksDF,left_on="Citizen_ID",right_on="Citizen_ID",how="inner")

# make object of data
BankAccounts = analyzer.Bank_Analyze(MergeDF,state)

# calculate mean, max and min loan amount
BankAccounts.calculater(mission_four_path)

# find account have condition for loan
BankAccounts.evaluate_loan()

# extarct accounts loan requsted approved
BankAccounts.Loan_Approved(mission_four_path)

# extract accounts with red flag
BankAccounts.red_accounts(mission_four_path)

# draw pie chart of percentage
BankAccounts.pie_chart(mission_four_path)

# draw scatter chart of approved and rejected loans
BankAccounts.Scatter_chart(mission_four_path)