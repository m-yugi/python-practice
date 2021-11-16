n=int(input())
x=input()
arr=list(map(int,input().split(" ")))
y=''
print(arr)
for i in x:
    if arr[int(i)-1]<=int(i):
        y+=i
    else:
        y+=str(arr[int(i)-1])
print(y)