for i in range(mid+1,-1,-1):
    for j in range(n):
        if(j>=mid-i and j<=mid+i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()