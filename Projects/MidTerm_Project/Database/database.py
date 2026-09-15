import sqlite3 as sql
import os
import sys
sys.path.append("f://programming/Bootcamp//PYBC_MidtermProject")

database_path = "f://programming/Bootcamp//PYBC_MidtermProject//Database"

# Making Databases
def Database_Biuld(state):

    # animals databse
    from Alaie_State_Analyzer.DataCleaning import animals_Cleaning  as animal

    conn = sql.Connection(os.path.join(database_path,f"{state}_DataBase.db"))
    cursor = conn.cursor()
   
   # data cleaning
    animal.ReadFile(state)
    animal.Clean()

    # make table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Animals (
                Animal_ID TEXT PRIMARY KEY,
                Species TEXT,
                Weight_kg INTEGER,
                Latitude INTEGER,
                Longitude INTEGER,
                Virus_Signature TEXT)
    ''')

    # find viral animals
    animal.unclean_animals()
    ListAnimals = animal.unclean.values

    # insert valuse
    cursor.executemany('''
    INSERT INTO Animals VALUES (
                    ?,?,?,?,?,?)
    ''',ListAnimals)


    # hospital database
    from Alaie_State_Analyzer.DataCleaning import Hospital_Cleaning as hospital

    # data cleaning
    hospital.ReadFile(state)
    hospital.Clean()


    # make table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Hospital (
                Record_ID TEXT PRIMARY KEY,
                Citizen_ID TEXT,
                Admission TEXT,
                Body_Temperature INTEGER,
                Syptoms INTEGER,
                Is_Viral BOOLEAN,
                Patient_DNA_Sample TEXT)
    ''')


    # insert values
    ListHospital = hospital.HospitalDF.values
    cursor.executemany('''
    INSERT INTO Hospital VALUES (
                    ?,?,?,?,?,?,?)
    ''',ListHospital)


    # citizen database
    from Alaie_State_Analyzer.DataCleaning import Citizens_Cleaning as Citizen

    # data cleaning
    Citizen.ReadFile(state)
    Citizen.Clean()

    # make table 
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Citizens (
                Citizen_ID TEXT PRIMARY KEY,
                First_Name TEXT,
                Last_Name TEXT,
                Age INTEGER,
                Phone_Number TEXT,
                Email TEXT,
                Address TEXT,
                Job_Title TEXT,
                Monthly_Income INTEGER,
                Total_Assets INTEGER)
    ''')


    # insert values
    ListCitizen = Citizen.CitizensDF.values

    cursor.executemany('''
    INSERT INTO Citizens VALUES (
                    ?,?,?,?,?,?,?,?,?,?)
    ''',ListCitizen)



    # store database
    from Alaie_State_Analyzer.DataCleaning import Store_Cleaning as store

    # database cleaning
    store.ReadFile(state)
    store.Clean()

    # make table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Store_Purchases (
                Purchases_ID TEXT PRIMARY KEY,
                Citizen_ID TEXT,
                Store_Name TEXT,
                Store_Address TEXT,
                Product_Catgory TEXT,
                Purchase_Amount INTEGER,
                Transacation_Time TEXT,
                Payment_Method TEXT)
    ''')

    # insert values
    ListStore = store.StoreDF.values
    cursor.executemany('''
    INSERT INTO Store_Purchases VALUES (
                    ?,?,?,?,?,?,?,?)
    ''',ListStore)


    # bank database
    from Alaie_State_Analyzer.DataCleaning import Bank_Cleaning as bank

    # data cleaning
    bank.ReadFile(state)

    # make table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Banks (
                Account_ID TEXT PRIMARY KEY,
                Citizen_ID TEXT,
                Currunt_Balance INTEGER,
                Loan_Request INTEGER,
                Missed_Payments INTEGER,
                Credit_Score INTEGER)
    ''')


    # insert values
    ListBank = bank.BankDF.values

    cursor.executemany('''
    INSERT INTO Banks VALUES (
                    ?,?,?,?,?,?)
    ''',ListBank)



    # traffic database
    from Alaie_State_Analyzer.DataCleaning import Traffic_Cleaning as traffic

    # data cleaning
    traffic.ReadFile(state)
    traffic.Clean()

    # make table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Police_Traffic (
                Log_ID TEXT PRIMARY KEY,
                License_Plate TEXT,
                Owner_Citizen_ID TEXT,
                Car_Model TEXT,
                Car_Color TEXT,
                Spped_km INTEGER,
                Speed_Limit INTEGER,
                Is_Reported_Stolen BOOLEAN,
                Camera_Address TEXT,
                Date_Time TEXT)
    ''')


    # insert values 
    ListTraffic = traffic.TrafficDF.values
    cursor.executemany('''
    INSERT INTO Police_Traffic VALUES (
                    ?,?,?,?,?,?,?,?,?,?)
    ''',ListTraffic)

    
    conn.commit()
    conn.close()


# make database
State_List = ["State_01","State_02","State_03","State_04","State_05","State_06","State_07",
              "State_08","State_09","State_10","State_11","State_12","State_13","State_14","State_15"]
for i in State_List :
    Database_Biuld(i)

