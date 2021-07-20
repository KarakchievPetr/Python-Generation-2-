with open("numbers.txt") as f:
    list_s = f.readlines()
    list_s = list(map(lambda x: x.strip().split(), list_s))
    list_s = list(map(lambda x: map(lambda y: int(y), x), list_s))
    print(list_s)
    summ = list(map(sum, list_s))
    print(*summ, sep ="\n")