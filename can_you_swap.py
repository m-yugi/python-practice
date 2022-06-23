for i in range(int(input())):
    n=int(input())
    s=input()
    res=''.join(sorted(s))
    count=0
    for j in range(n):
        if(res[j]!=s[j]): count+=1
    if(count==2 or n<=1 ):
        print("YES")
    else:
        print("NO") 