s=input()
m=int(input())
l=list(map(int,input().split()))
l.sort()
count=0
for i in range(1, m):
    if(l[i] >= sum(l[0:i])):
        count += 1
    elif(sum(l[0:i]) > l[m-1]):
        print(count)
    else:
        for j in range(i, m):
            if(l[j] >= sum(l[0:i])):
                count += 1
                l[i], l[j] = l[j], l[i]
                break
print(count)