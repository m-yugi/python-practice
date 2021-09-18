nums = [-1,0,3,5,9,12]
n=len(nums)
target = 9
l=0
r=n-1
while(l<=r):
    pivot=l+(r-l)//2
    if(nums[pivot]==target):
        print(pivot)
    if(target<nums[pivot]):
        r=pivot-1
    else:
        l=pivot+1
print("-1")