with open("population.txt") as f:
    list_s = f.readlines()
    list_s = list(map(lambda x: x.strip().split("\t"), list_s))
    list_s = list(filter(lambda x: x[0][0] =="G" and int(x[1]) > 500000, list_s ))
    for i in list_s:
        print(i[0])