def evenpositions(l):
    if(len(l)==0):
        return []
    else:
        return [l[i] for i in range(len(l)) if i%2==0]
l=[1,2,3,4,5]
print(evenpositions(l))