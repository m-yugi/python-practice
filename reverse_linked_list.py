head=[1,2,3,4,5]
num=len(head)
mid=num//2
j=num-1
for i in range(mid):
    temp=head[i]
    head[i]=head[j]
    head[j]=temp
    j-=1
print(head)
