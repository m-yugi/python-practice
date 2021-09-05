#works for any input
height=[1,8,6,2,5,4,8,3,7]
result =0
l, r = 0, len(height)-1
while l < r:
    result = max(result, min(height[l], height[r]) * (r-l))
    if height[l] < height[r]: l += 1
    elif height[r] <= height[l]: r -= 1
               
print(result)