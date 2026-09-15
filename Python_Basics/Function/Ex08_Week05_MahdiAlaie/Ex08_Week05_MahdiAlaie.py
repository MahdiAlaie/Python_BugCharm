def avr(NumList):
    SumN=0
    for i in NumList:
        SumN += i
    print(SumN/len(NumList))

numbers=[12,17,18,20,10]
avr(numbers)
