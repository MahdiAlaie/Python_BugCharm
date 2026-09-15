def OE (x):
    if x % 2 == 0:
        return "The number is Even"
    else:
        return "The number is Odd"

num=OE(int(input("please enter a number:")))
print(num)