for i in range(int(input())):
        c,p=map(int,input().split())
        l=[0]*c
        for j in range(c):
            for k in range(j,c):
                if(p>0):
                    l[k]+=1
                    p-=1
                else:
                    break
        if(p>0):
            l[0]+=p
        for m in l:
            print(m,end=" ")
        print()