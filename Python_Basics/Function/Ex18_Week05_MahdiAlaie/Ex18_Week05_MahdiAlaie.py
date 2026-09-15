def leastelement(list):
    least = list[0]
    for i in list:
        if i < least :
            least = i
    print(least)
result = [3,45,67,23,57,89]
leastelement((result))