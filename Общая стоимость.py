with open("prices.txt") as f:
    a = [i.split("\t")for i in f.readlines()]
    print(sum(map(lambda x: int(x[2])*int(x[1]),a)))
    