import re

with open("tz.txt") as f1, open("forbidden_words.txt") as f2:   
    dct = []
    for line in f2:
        sp =line.split()
        for i in sp:
            dct.append(i)
    dct.sort(key=len, reverse =False)
    for line in f1:
        line = line.strip()
        text =line.split()
        for j in range(len(text)):
            for i in dct:
                text[j] = re.sub(i, "*"*len(i), text[j],  flags=re.IGNORECASE)         
        print(*text, sep=" ") 