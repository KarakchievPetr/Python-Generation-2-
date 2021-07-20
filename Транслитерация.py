d = {
    '�': 'a', '�': 'k', '�': 'h', '�': 'b', '�': 'l', '�': 'c', '�': 'v', '�': 'm', '�': 'ch',
    '�': 'g', '�': 'n', '�': 'sh', '�': 'd', '�': 'o', '�': 'shh', '�': 'e', '�': 'p', '�': '*',
    '�': 'jo', '�': 'r', '�': 'y', '�': 'zh', '�': 's', '�': "'", '�': 'z', '�': 't', '�': 'je',
    '�': 'i', '�': 'u', '�': 'ju', '�': 'j', '�': 'f', '�': 'ya'
    }
with open("cyrillic.txt", encoding='utf-8') as f, open("transliteration.txt", "w", encoding='utf-8') as o:
    for i in f:
        for j in range(len(i)):
            if i[j] in d:
                i = i.replace(i[j], d[i[j]])
            elif i[j].lower() in d:
                if  len(d[i[j].lower()]) == 1:
                    i = i.replace(i[j], d[i[j].lower()].upper())
                else:
                    i = i.replace(i[j], d[i[j].lower()][0].upper()+d[i[j].lower()][1])
        print(i, end ="")
        print(i, file=o)