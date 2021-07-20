name = "t21.txt"
with open(name, encoding='utf-8') as f:
    text = f.read()
    text = text.split("def")
    sp = []
    for i in range(len(text)-1):
        if not "#" in text[i]:
            a1 = text[i+1].find(" ")
            a2 = text[i+1].find("(")
            text1 = text[i+1][a1+1:a2]
            sp.append(text1)
    if len(text)-1 == len(sp):
        print("Best Programming Team")
    else:
        print(*sp, sep="\n")

    
            
