d=dict()
key=[]
with open('orders.csv',encoding='utf-8') as f:
    f.readline()
    for i in f:
        key=list(map(str.strip,i.split(',')))
        print(key[0])
        if key[0] in d:
            d[key[0]].append(key[1:])
            print(d[key[0]])
        else:
            d[key[0]]=[key[1:]]
            print(d[key[0]])

def qwe(d):
    for i in d:
        try:
            float(d[i][0][0])
            print(d[i][0][0])
            return
        except:
            pass# как работать с try и except
        newk = dict()
        for f in d[i]:
            if f[0] in newk:
                newk[f[0]].append(f[1:])
                #print(newk[f[0]])
            else:
                newk[f[0]] = [f[1:]]
                #print(newk[f[0]])
        '''print(newk)'''
        d[i] = newk
        qwe(d[i])
print(d)
qwe(d)
print(d)
for r in d:
    for i in d[r]:
        for j in d[r][i]:
            d[r][i][j]={'price':d[r][i][j][0][1],'qunt':d[r][i][j][0][0]}
print(d)
