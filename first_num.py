count = 0
for i in range(len(arr)):
    for j in range(i, len(arr)):
        if i != j and (arr[i]+arr[j] >= l and arr[i]+arr[j] <= r):
            count += 1
return count