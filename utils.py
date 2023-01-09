import csv

def init():
    with open('words.csv', newline='', encoding='utf-8-sig') as csvfile:
        rows = csv.reader(csvfile)
        rows = list(rows)
        header = rows[0]
        
        dic = {}
        for c in range(len(header)):
            if header[c] == "":
                continue
            for r in range(1, len(rows)):
                word = rows[r][c]
                if word != "":
                    dic[word] = header[c]
                    
        print(dic)
                    

    