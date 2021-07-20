from random import randint
with open("first_names.txt") as f1, open("last_names.txt") as f2:
    names = list(map(lambda x: x.strip(),f1.readlines()))
    lnames = list(map(lambda x: x.strip(),f2.readlines()))
    for i in range(3):
        print(f'{names[randint(0,len(names))-1]} {lnames[randint(0,len(lnames))-1]}')