row=10
for i in range(0,row):
    for j in range(0,row):
        if(i==j or j==row-1-i):
            print("*",end="")
        else:
            print("-",end="")
    print()