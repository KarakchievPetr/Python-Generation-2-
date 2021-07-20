with open("nums.txt") as f:
    list_s = f.readlines()
    list_s = list(map(lambda x: "".join(list(map(lambda y: y if y.isdigit() else " ", x))), list_s))
    list_s = list(map(lambda x: x.split(), list_s))
    list_s = list(map(lambda x: sum(list(map(lambda y: int(y), x))), list_s))
    print(sum(list_s))
