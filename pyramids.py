n = int(input())

for i in range(n):
    for j in range(2*n+1):
        if j >= n-i and j <= n+i:
            print(i+1,end=" ")
        else:
            print("-", end=" ")
    print()
