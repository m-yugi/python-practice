arr=list(map(int,input().split(" ")))
result=list(set(range(1,len(arr)+1))-set(arr))
print(result)