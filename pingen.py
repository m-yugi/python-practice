n=int(input())
l=list(input().split(" "))
k=int(input())
l2=[]
count=0
sum=0
for i in l:
    if(count!=k):
        sum+=int(i)
        count+=1
    else:
        l2.append(sum)
        print(sum)
        sum=0
        count=0
l2.append(sum)
print(l2)