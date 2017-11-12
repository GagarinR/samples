def listsort(arr):
    tmp = []
    for i1, i in enumerate(arr):
        if i == -1:
            tmp.append(str(i) +'.'+ str(i1))
    lst = [x for x in arr if x != -1]
    lst.sort()
    for i in tmp:
        lst.insert(int(i.split('.')[1]), int(i.split('.')[0]))
    return lst

print (listsort ([7,-1,3,1,-1,4]))
