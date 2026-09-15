import numpy as np
import matplotlib.pyplot as plt
# Grid Size
feildX = 10
feildY = 10
feild = np.zeros((feildX,feildY))

# Broders
feild[0,:]=2
feild[-1,:]=2
feild[:,0]=2
feild[:,-1]=2

#Obstacles
NumOb = 10
rng = np.random.default_rng(np.random.randint(2,feildX-1))
ObX = rng.integers(2,feildX-1,NumOb)
ObY = rng.integers(2,feildY-1,NumOb)
for i in range(NumOb):
    feild[ObX[i],ObY[i]]=5

SnakeX=[1,1,1,1]
SnakeY=[1,2,3,4]
feild[SnakeX[-1],SnakeY[-1]]=4
for s in range(len(SnakeX)-1):
    feild[SnakeX[s],SnakeY[s]]=3

RngSeed = np.random.default_rng(np.random.randint(2,feildX-1))  
PrizeX = RngSeed.integers(2,feildX-1)
PrizeY = RngSeed.integers(2,feildY-1)

def NewPrize ():
    global PrizeX,PrizeY
    while ((PrizeX in ObX) and (PrizeY in ObY)) or ((PrizeX in SnakeX) and (PrizeY in SnakeY)):
        PrizeX = RngSeed.integers(2,feildX-1)
        PrizeY = RngSeed.integers(2,feildY-1)
    feild[PrizeX,PrizeY]=1




def Direction (array,unit):
        array[0]=feild[SnakeX[-1]-unit,SnakeY[-1]]
        array[1]=feild[SnakeX[-1]+unit,SnakeY[-1]]
        array[2]=feild[SnakeX[-1],SnakeY[-1]+unit]
        array[3]=feild[SnakeX[-1],SnakeY[-1]-unit]



NewPrize()

PrizeCounter = 0
StepCounter = 0
dead = False

for i in range(140):
    
    RandDirect = np.random.randint(0,4)
    SelectDirect = np.array([0,0,0,0]) #LRDU                 
    Direction(SelectDirect,1)

    while SelectDirect[RandDirect]>1:
        if not ( 0 in SelectDirect or 1 in SelectDirect):
            print("GAME OVER")
            dead = True
            break
        if PrizeX > SnakeX[-1]:
            RandDirect = 1
        elif PrizeX < SnakeX[-1]:
            RandDirect = 0
        elif PrizeY > SnakeY[-1]:
            RandDirect = 2
        elif PrizeY < SnakeY[-1]:
            RandDirect = 3
        else:
            RandDirect = np.random.randint(0,4)
       
     
    if dead:
        break
        

    def UpdateFeild ():
        for b in range(len(SnakeX)-1):
            SnakeX[b] = SnakeX[b+1]
            SnakeY[b] = SnakeY[b+1]

    if SelectDirect[RandDirect]==1:
        if RandDirect == 0:
            SnakeX.append(SnakeX[-1]-1)
            SnakeY.append(SnakeY[-1])
        elif RandDirect == 1:
            SnakeX.append(SnakeX[-1]+1)
            SnakeY.append(SnakeY[-1])
        elif RandDirect == 2:
            SnakeX.append(SnakeX[-1])
            SnakeY.append(SnakeY[-1]+1)
        elif RandDirect == 3:
            SnakeX.append(SnakeX[-1])
            SnakeY.append(SnakeY[-1]-1)
        NewPrize()
        PrizeCounter += 1
    
    for s in range(len(SnakeX)):
            feild[SnakeX[s],SnakeY[s]]=0

    
    UpdateFeild()
    if RandDirect == 0:
        SnakeX[-1] -= 1
        plt.title(f"Went UP!")
        StepCounter += 1
    elif RandDirect == 1:
        SnakeX[-1] += 1
        StepCounter += 1
        plt.title(f"Went DOWN!")
    elif RandDirect == 2:
        SnakeY[-1] += 1
        StepCounter += 1
        plt.title("Went RIGHT!")
    elif RandDirect == 3:
        SnakeY[-1] -= 1
        StepCounter += 1
        plt.title("Went LEFT!")

    for s in range(len(SnakeX)-1):
        feild[SnakeX[s],SnakeY[s]]=3

    feild[SnakeX[-1],SnakeY[-1]]=4

    plt.imshow(feild,colorizer="cyan")
    plt.pause(0.3)
    plt.clf()
    plt.title(f"{StepCounter} Steps!",loc="right")
    plt.title(f"Score is {PrizeCounter}",loc="left")
    



StepCounter = 0
PrizeCounter = 0


