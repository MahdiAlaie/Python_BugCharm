def password (pas):
    if len(pas.strip()) < 8 :
        return"password can't be less 8 charachter"
    elif "password" in pas :
        return"you can't use 'password' in your password"
    else:
        return "signed in"

Userpassword= password(input("Please enter a password:"))
print(Userpassword)