with open("words.txt") as f:
    sp = f.readline().split()
    max_len = max(list(map(lambda x:len(x), sp)))
    sp_new = list(filter(lambda x: len(x) ==max_len, sp ))
    print(*sp_new, sep ="")