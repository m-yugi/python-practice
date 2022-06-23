from math import ceil, floor
for _ in range(int(input())):
    r= int(input())
    if(r%2==0):
        r-=1
    for i in range(1, ceil(r/2)):
        for j in range(1,r-i+1):
            print("-", end="")
        for j in range(1, 2*i):
            if j==1 or j==2*i-1:
                print("*", end="")
            else:
                print("-", end="")
        print()
    for i in range(ceil(r/2),0, -1):
        for j in range(1,r-i+1):
            print("-", end="")
        for j in range(1, 2*i):
            if j==1 or j==2*i-1:
                print("*", end="")
            else:
                print("-", end="")
        print()