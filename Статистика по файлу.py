from functools import reduce
with open("file1.txt") as f:
    list_s = f.readlines()
    list_s = list(map(lambda x: x.strip(), list_s))
    z = len(list_s)
    y = sum(map(lambda x: len(x.split()), list_s ))
    x = sum(map(lambda x: len(list(filter(lambda y: y.isalpha(), x))), list_s))
    print(f"""Input file contains:
{x} letters 
{y} words 
{z} lines""")
