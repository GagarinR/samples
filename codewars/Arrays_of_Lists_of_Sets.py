    
s1 = ["abc","abbc","ab","xyz","xy","zzyx"]#),[1,8])
s2 = ['wkskkkkkk','fokoo','wkskk','uizzzz','fokooff','wkskkkk','uizzzzzzz']#),[5,7,9])

def solve(arr):    
    arr=[''.join(set([i2 for i2 in i])) for i in arr]
    
    r=[]
    for c, i in enumerate(arr):
        for c2, i2 in enumerate(arr):
            if i == i2:
                 r.append({i2: c2})

    new_arr =  [i.keys()[0] for i in r]
    new_arr = [i for i in new_arr if new_arr.count(i)==1 ]
    
    r2 =[]
    for i in r:
        if i not in r2:
            r2.append(i)

    t = dict()
    for i in r2:
        if i.keys()[0] not in t.keys(): t[i.keys()[0]] = i[i.keys()[0]]
        else: t[i.keys()[0]]+=i[i.keys()[0]]

    for i in new_arr: 
        del t[i]
    
    return sorted([t[i] for i in t])
    
print solve(s1)

###########################################################################
###########################################################################
###########################################################################
###########################################################################
###########################################################################



def solve(arr): 
    arr=[''.join(set([i2 for i2 in i])) for i in arr]
    print arr

    r=[]

    for c, i in enumerate(arr):
        for c2, i2 in enumerate(arr):
            if i == i2:
                 r.append({i2: c2})

    print r, 'all variations'

    new_arr =  [i.keys()[0] for i in r]
    # print [i for i in new_arr if new_arr.count(i)==1 ]
    new_arr = [i for i in new_arr if new_arr.count(i)==1 ]

    # print e
    r2 =[]
    for i in r:
        if i not in r2:
            r2.append(i)

    t = dict()
    for i in r2:
        if i.keys()[0] not in t.keys():
            t[i.keys()[0]] = i[i.keys()[0]]
        else:
            t[i.keys()[0]]+=i[i.keys()[0]]


    print t


    for i in new_arr:
        del t[i]

    print t
    # print [i for i in t if i not in new_arr]
    return sorted([t[i] for i in t])
