d = {
    'à': 'a', 'ê': 'k', 'õ': 'h', 'á': 'b', 'ë': 'l', 'ö': 'c', 'â': 'v', 'ì': 'm', '÷': 'ch',
    'ã': 'g', 'í': 'n', 'ø': 'sh', 'ä': 'd', 'î': 'o', 'ù': 'shh', 'å': 'e', 'ï': 'p', 'ú': '*',
    '¸': 'jo', 'ð': 'r', 'û': 'y', 'æ': 'zh', 'ñ': 's', 'ü': "'", 'ç': 'z', 'ò': 't', 'ý': 'je',
    'è': 'i', 'ó': 'u', 'þ': 'ju', 'é': 'j', 'ô': 'f', 'ÿ': 'ya'
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