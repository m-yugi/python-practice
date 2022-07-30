def printSubArrays(arr, start, end, B):
    if end == len(arr):
        return
    elif start > end:
        return printSubArrays(arr, 0, end + 1, B)
    else:
        B.append(sum(arr[start:end + 1]))
        return printSubArrays(arr, start + 1, end, B)


def Kthlargest(N, K, A):
    B = []
    printSubArrays(A, 0, 0, B)
    B.sort()
    return (B[K-1])


print(Kthlargest(10, 3, [1, 3, 4]))
