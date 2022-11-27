for i in range(int(input())):
    arr = []
    for i in range(int(input())):
        arr.append(int(input()))
    for i in range(1, len(arr)):
        if(arr[i] % 2 == 0 and arr[i-1] % 2 != 0):
            print("NO")
        elif(arr[i] % 2 != 0 and arr[i-1] % 2 == 0):
            print("NO")
    print("YES")
