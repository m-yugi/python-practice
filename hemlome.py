n=int(input("please enter the an odd value\n"))
mid=n//2
for i in range(mid+1):
    for j in range(n):
        if(j>=mid-i and j<=mid+i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(mid-1,-1,-1):
    for j in range(n):
        if(j>=mid-i and j<=mid+i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()