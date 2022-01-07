n=int(input())
cost=[]
for i in range(n):
    cost.append(int(input()))
m=int(input())
labels=[]
for i in range(m):
    labels.append(input())
dailyCount=int(input())
counter=0
j=0
sumi=0
l=[]
for i in labels:
    if i=="legal" and counter<dailyCount:
        sumi+=cost[j];
        counter+=1;
    elif(i=="illegal"):
        sumi+=cost[j]
    else:
        l.append(sumi)
        counter=0
        sumi=0
    j+=1
maxi=max(l)
print(maxi)