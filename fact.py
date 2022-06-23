m={}
def fun(n):
    if(n==0 or n==1): return 1
    if n in m.keys(): return m[n]
    m[n]=n*fun(n-1)
    return m[n]
for _ in range(int(input())):
    n=int(input())
    print(fun(n)%1000000007)