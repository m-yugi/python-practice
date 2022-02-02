n=int(input())
l=[]
for i in range(n):
    l.append(0)
m=int(input())
buckets_filled=0
for i in range(m):
    q=int(input())
    if q==1:
        for i in range(n):
            l[i]=1
    elif q==2:
        for i in range(n):
            if i%2==0:
                l[i]=0
    elif q==3:
        for i in range(n):
            if(i%2!=0):
                l[i]=0
    else:
        for i in range(n):
            l[i]=0
for i in l:
    if(i==1):
        buckets_filled+=1
if n%2==0:
    print(buckets_filled)
else:
    print(buckets_filled-1)