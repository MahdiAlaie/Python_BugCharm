votes = ["Candidate A", "Candidate B", "Candidate A", "Candidate C", "Candidate A","Candidate B"]
FindWinner={

}
winnername=''
maxvote=0
for i in votes:
    FindWinner[i]= FindWinner.get(i,0)+1

for con,value in FindWinner.items():
    if value > maxvote:
        maxvote=value
        winnername=con
        print(f"{con} is the winner")
print(FindWinner)    

