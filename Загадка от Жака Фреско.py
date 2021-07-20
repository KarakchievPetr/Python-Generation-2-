# put your python code here
with open("goats.txt") as f, open("answer.txt", "w") as o:
    i = 1
    flag = 0
    goats = {}
    summ = 0
    ans = []
    for line in f:
        line = line.strip()
        if flag == 0 and line != "COLOURS" and line != "GOATS":
            goats[line] = 0
        if flag == 1:
            goats[line] += 1
            summ +=1
        if line == 'GOATS':
            flag = 1
    for i in goats:
        if round(goats[i] /summ*100, 2) > 7:
            ans.append(i)
    print(*sorted(ans), sep="\n", file=o)