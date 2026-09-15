def temperature(x):
    if x>=38:
        return "Warning!, The temperature is too high"
    else:
        return "OK!"
    

temp=temperature(int(input("Please enter machine temperature:")))
print(temp)