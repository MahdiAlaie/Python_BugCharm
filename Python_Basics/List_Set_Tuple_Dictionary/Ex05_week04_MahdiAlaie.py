files = ["report.pdf", "image.png", "data.csv", "logo.png", "notes.txt","thesis.pdf"]
SortByExtention={

}

for i in files:
    ext=i.split('.')[-1]
    if ext not in SortByExtention:
        SortByExtention[ext]=[]
    SortByExtention[ext].append(i)
       
print(SortByExtention)
