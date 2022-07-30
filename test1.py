row = int(input())
col = int(input())
l=[]
for i in range(row):
    a =[]
    for j in range(col):
         a.append(int(input()))
    l.append(a)
dum=[]
for i in range(row):
    a =[]
    for j in range(col):
         a.append(l[i][j])
    dum.append(a)
for i in range(row):
    for j in range(col):
        if(l[i][j]==0):
            for k in range(col):
                dum[i][k]=0
            for m in range(row):
                dum[m][j]=0
for i in range(row):
    for j in range(col):
        print(dum[i][j],end=" ")
    print()