import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import csv
import os

class Bank_Analyze:
    
    def __init__(self,dataframe,state):
        self.df = dataframe
        self.state = state
    
    # To evluate which accuont have condithions to get loan
    def evaluate_loan(self):

        # filter data loan reques amount = 0
        self.df = self.df.loc[self.df["Loan_Request"]>0,:]

        # filter data red flaged accounts 
        self.df["Loan_Status"] = np.where((self.df["Missed_Payments"] >= 6),False,False)
        self.df["Loan_Status"] = np.where((self.df["Credit_Score"]<500),False,False)
        
        # filter data loan approve conditions
        self.df["Loan_Status"] = np.where((self.df["Credit_Score"]>500)&(self.df["Missed_Payments"] < 6)&(self.df["Loan_Request"]<(self.df["Currunt_Balance"]+self.df["Total_Assets"])*0.6),True,False)
    
    # Extarct accounts loan requests approved
    def Loan_Approved(self,path):

        # filter data
        self.approverd = self.df.loc[self.df["Loan_Status"]==True,["Account_ID","Loan_Request"]]
        self.approverd = self.approverd.values
        
        # extarct data
        with open (os.path.join(path,f"{self.state}_Loan_Approved.csv"), "w" , newline="" ) as cvsfile:
            writer = csv.writer(cvsfile)
            writer.writerows(self.approverd)

    # flag accounts have missed payment over 6 or credit score less than 500 and extarct data
    def red_accounts(self,path):

        # filter data
        self.red_flag_account = self.df.loc[(self.df["Missed_Payments"] >= 6) | (self.df["Credit_Score"]<500),["Citizen_ID","First_Name","Last_Name","Phone_Number","Account_ID","Total_Assets"]]
        
        # extarct data
        self.red_flag_account.to_csv(os.path.join(path,f"{self.state}_Red_Flagged_Accounts.csv"))

    # draw a pie chart on percntage of approved and rejected loans
    def pie_chart(self,path):

        #calcute percentages
        self.Loan_Approved_percentage = self.df["Loan_Status"].mean()*100
        self.Loan_Rejected_percentage = 100 - self.Loan_Approved_percentage

        #calculate sum payment
        self.approved_df = self.df.loc[self.df["Loan_Status"]== True,:]
        self.total_paid = self.approved_df["Loan_Request"].sum()
        self.peaple_count = self.approved_df.shape[0]
        
        #pie chart setting
        percentage = [self.Loan_Approved_percentage,self.Loan_Rejected_percentage]
        labels = [f"Approved({self.Loan_Approved_percentage:.1f}%)",f"Rejected({self.Loan_Rejected_percentage:.1f}%)"]
        colors = ["green", "red"]
        explode = (0.1,0)
        report = f"Total Payment: {self.total_paid:.1f}\nNumber of people to pay: {self.peaple_count}"

        # draw the chart
        plt.figure()
        plt.pie(percentage,labels=labels,colors=colors,shadow=True,explode=explode)
        plt.title("Loan Approval Distributions")
        plt.text(-0.05,-0.05,report,
                 transform=plt.gca().transAxes,
                 ha="left",
                 va="bottom",
                 bbox= dict(facecolor = "white",alpha=0.7,edgecolor="black"))
        plt.savefig(os.path.join(path,f"{self.state}_Loan Approval Distributions"))

    # draw a scatter chart by loan amount and credit score domain
    def Scatter_chart(self,path):
          
          # filter approved loan data
          self.approved_credit = self.df.loc[self.df["Loan_Status"]==True,"Credit_Score"]  
          self.approved_loan_amoont = self.df.loc[self.df["Loan_Status"]==True,"Loan_Request"]
         
          # filter rejected loan data
          self.rejected_credit = self.df.loc[self.df["Loan_Status"]==False,"Credit_Score"]  
          self.rejected_loan_amoont = self.df.loc[self.df["Loan_Status"]==False,"Loan_Request"]
         
         # draw chart
          plt.figure()

          # approved loan
          plt.scatter(self.approved_credit,self.approved_loan_amoont,c="green",marker="o",alpha=0.6,label="Approved")
          
          # rejected loan 
          plt.scatter(self.rejected_credit,self.rejected_loan_amoont,c="red",marker="x",alpha=0.6,label="Rejected")
          
          # chart setting
          plt.title("Credit Score VS Loan Amount")
          plt.xlabel("Credit Score")
          plt.ylabel("Loan Amount")
          plt.legend(loc="upper right")
          plt.savefig(os.path.join(path,f"{self.state}_Scatter_Chart"))
    
    # To calculate mean , max and min loan requsted amount
    def calculater(self,path):

        # filter loan amount = 0
        self.df = self.df.loc[self.df["Loan_Request"]>0,:]
        
        # filter mean , max and min loan amount as Dict
        self.calculate = {"Metric": ["Mean","Maximum","Minimum"],
                        "Value" : [np.mean(self.df["Loan_Request"]),np.max(self.df["Loan_Request"]),np.min(self.df["Loan_Request"])]}
        self.dataframe = pd.DataFrame(self.calculate)
        
        # extract data
        self.dataframe.to_csv(os.path.join(path,f"{self.state}_Mean_Max_Min.csv"))