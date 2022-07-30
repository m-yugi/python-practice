A=[[1,1,1],[2,2,2],[3,3,3]]
d={}
for i in A[0]:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
B=[]
for i in A[0]:
    B.append(d[i]-1)
print(B)