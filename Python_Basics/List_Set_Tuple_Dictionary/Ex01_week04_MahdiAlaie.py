DnaSequence = "ATGTCGATGTGCATGTCGATG"
FirstStepCounter=0
SecondStepCounter=3
DnaSequenceList=[]
DnaSequenceDict={

}

for i in range(0,len(DnaSequence),3):
     DnaSequenceList.append(DnaSequence[FirstStepCounter:SecondStepCounter])
     FirstStepCounter+=3
     SecondStepCounter+=3

for x in DnaSequenceList:
     DnaSequenceDict[x]=DnaSequenceDict.get(x,0)+1

for key,value in DnaSequenceDict.items():
     if value > 1:
          print(f'{key}:{value}')
print(DnaSequenceDict)

