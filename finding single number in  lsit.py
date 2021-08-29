nums=list(map(int,input().split()))
result=0
for i in nums:
    result=result^i
print(result)