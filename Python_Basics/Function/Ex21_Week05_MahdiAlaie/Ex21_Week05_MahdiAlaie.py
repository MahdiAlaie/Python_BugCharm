RawData=[12.5, -1, 14.0, 15.2, -5, 13.8]
def ToN (list):
    for i in list:
        if i < 0:
            list.remove(i)
    return list
NewList=ToN(RawData)
print(NewList)