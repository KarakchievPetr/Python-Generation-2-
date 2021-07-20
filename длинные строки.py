with open("lines.txt") as f:
    list_s = f.readlines()
    list_s = list(map(lambda x: x.strip(), list_s))
    m_l = list(filter(lambda x:len(x) == len(max(list_s)), list_s))
    print(*m_l, sep ="\n")