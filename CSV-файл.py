def read_csv():
    with open('data.csv') as f:
        i = 0
        sp = []
        for line in f:
            line =line.strip()
            if i  == 0:
                keys = line.split(",")
            else:
                values = line.split(",")
                sp.append({keys[i] : values[i] for i in range(len(keys))})
            i +=1
        return sp  
