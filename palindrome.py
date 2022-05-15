def pesudo(n,s):
    l=0
    e=0
    n-=1
    for i in range(n//2):
        l+=int(s[i])
        e=int(s[n])
        n-=1
    if(abs(l-e)>122):
        return 0
    else:
        return 1
n=8
s="odrcrdqo"
print(pesudo(n,s))