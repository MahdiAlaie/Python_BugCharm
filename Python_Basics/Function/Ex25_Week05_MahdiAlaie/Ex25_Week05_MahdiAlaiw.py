txt= "Lorem ipsum dolor site amet, consectetur adipiscing elit"
txt = txt.replace(",","")

def LetterCounter (text):
    textchardict={

    }
    txtList = text.split(" ")
    for i in txtList:
        if len(i) not in textchardict:
            textchardict[len(i)]=[]
        textchardict[len(i)].append(i)
    return textchardict
texchar = LetterCounter(txt)
print(texchar)


    