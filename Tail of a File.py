with open("last_names.txt") as f:
    sp = f.readlines()
    length = len(sp)
    if length >10:
        print(*sp[length-10:], sep ="")
    else:
        print(*sp, sep ="")