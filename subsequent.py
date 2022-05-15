def lengthOfLIS(self, nums):       
    dp = [1] * len(nums) 
    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[i] >= nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(dp)
    return max(dp)
n=int(input())
a=[int(input()) for i in range(n)]
k=int(input())
num=lengthOfLIS(type,a)
print(num)