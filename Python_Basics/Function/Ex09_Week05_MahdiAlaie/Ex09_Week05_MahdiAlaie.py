def sumsub(x,y):
    if x>y:
        return x-y
    else:
        return x+y
    
num= sumsub(int(input("Please enter a number:")),int(input("Please enter a number:")))
print(num)