def jump1(nums,n,jump):
        if n==1:
            return True
        else:
            for i in range(n):
                jump=max(jump,nums[i])
                if(jump==0 and i!=n-1):
                     return False
                jump-=jump
        return True
#runs for any input
nums=[3,2,1,0,4]
n=len(nums)
jump=0
print(jump1(nums,n,jump))