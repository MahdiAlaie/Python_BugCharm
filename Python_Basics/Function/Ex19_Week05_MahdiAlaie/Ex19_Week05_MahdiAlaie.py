def new_dict ():
    dict = {

    }
    for i in range(0,5):
        name = input("Please enter your name:")
        age = input("Please enter your age:")
        dict[name]= age

    return dict 
UserDict=new_dict()
print(UserDict)