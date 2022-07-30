arr = [1.90, 1.04, 1.25, 2.5, 1.75]
arr.sort()
print(arr)
i = 0
time = 0
count = 0
while(i < len(arr)):
    time += arr[i]
    print(time)
    if time <= 3.00:
        i += 1
    else:
        time = 0
        count += 1
# if time != 0 and time <= 3.00:
#     return count = 1
# return count
