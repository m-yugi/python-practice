def listdiff(l1,l2):
    ldiff1=[]
    ldiff2=[]
    for i in l1:
        if i not in l2:
            ldiff1.append(i)
    for i in l2:
        if i not in l1:
            ldiff2.append(i)
    return ldiff1,ldiff2
l1=list(map(int,input().split(' ')))
l2=list(map(int,input().split(' ')))
print(listdiff(l1,l2))
