n, k = map(int, input().split())
if(n != 0):
    m = list(map(int, input().split()))
    res = ""
    for _ in range(k):
        ind, val = map(int, input().split())
        m[ind-1] = val
        sumi = 1
        for i in range(1, len(m)):
            if(m[i-1] != m[i]):
                sumi += 1
        res += str(sumi) + " "
    if(res):
        print(res)
    else:
        print(0)
else:
    print(0)
