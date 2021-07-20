with open("data.txt") as f:
    list_s = f.readlines()
    list_s = list(map(lambda x: x[:-1], list_s))
    print(*reversed(list_s), sep="\n")
