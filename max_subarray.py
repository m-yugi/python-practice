nums=list(map(int,input().split()))
maxsum=nums[0]
cursum=0
for i in nums:
    if(cursum<0):
        cursum=0
    cursum+=i
    maxsum=max(cursum,maxsum)
print(maxsum)