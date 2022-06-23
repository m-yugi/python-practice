n=int(input())
hi,l=n//2,n//2
for i in range(n):
    # print("i am i",i)
    for j in range(i):
        print("i am j",j)
        if((j==hi and j<=n-1) or (j==l and j<=0)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        hi+=1
        l-=1