import numpy as np
arr1=np.array([1,2,3,4,5])
arr2=np.array([6,7,8,9,10])
temp=arr1-arr2
distance=np.linalg.norm(temp)
print(distance)