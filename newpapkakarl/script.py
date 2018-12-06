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
for i in d:
    newk=dict()
    for f in d[i]:
        if f[0] in newk:
            newk[f[0]].append(f[1:])
            print(newk[f[0]])
        else:
            newk[f[0]]=[f[1:]]
            print(newk[f[0]])
    print(newk)
    d[i]=newk
print(d)
def qwe(d):
