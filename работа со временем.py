# put your python code here
import datetime as dt
def mins_hours(d1, d2):
    a1 = d1.split(":")
    h1 = int(a1[0])
    m1 = int(a1[1])
    a2 = d2.split(":")
    h2 = int(a2[0])
    m2 = int(a2[1])
    if (h2 - h1)*60+ (m2-m1) >= 60:
        return True
    else:
        return False
with open("l2.txt") as f, open("output.txt", "w") as o:
    for line in f:
        line = line.strip()
        sp = line.split(", ")
        if mins_hours(sp[1], sp[2]):
            print(sp[0], file = o)
