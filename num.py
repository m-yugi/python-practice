n=7
s=0
P=[True for k in range(n+1)]
p=2
P[0]=False
P[1]=False
for i in range(2,8,2):
    if(P[i]):
        s+=1
print(s)