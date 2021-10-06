nums1 = [1,2,2,1]
nums2 = [2,2]
n=len(nums1)
m=len(nums2)
mini=min(n,m)
ans=[]
if(mini==n):
    for i in nums1:
        if i in nums2:
            ans.append(i)
            nums2.remove(i)
else:
    for i in nums2:
        if i in nums1:
            ans.append(i)
            nums1.remove(i)
print(ans)