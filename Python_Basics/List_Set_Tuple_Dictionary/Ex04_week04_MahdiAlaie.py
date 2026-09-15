text = "Math is great. Math is fun! We Love Math."
text=text.replace("!","")
text=text.replace(".","")
text=text.lower()
text=text.split(" ")
WordCounter={

}
for x in text:
    WordCounter[x]=WordCounter.get(x,0)+1

print(WordCounter)