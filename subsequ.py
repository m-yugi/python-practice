n,m=map(int,input().split())
a=list(map(int,input().split()))
fcount=0
count=1
for i in range(1,n):
    # print(a[i-1],a[i])
    if(a[i-1]==a[i]):
        fcount=max(fcount,count)
        count=1
    else:
        count+=1
fcount=max(fcount,count)
if(fcount>=m):
    print(fcount)   