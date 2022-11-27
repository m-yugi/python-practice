N = int(input())
A = list(map(int, input().split()))
count = 1
A.sort()
for i in range(1, N):
    if(A[i] >= sum(A[0:i])):
        count += 1
    elif(sum(A[0:i]) > A[N-1]):
        print(count)
    else:
        for j in range(i, N):
            if(A[j] >= sum(A[0:i])):
                count += 1
                A[i], A[j] = A[j], A[i]
                break
print(count)