r,c=map(int,input().split())
l=[]
for i in range(r):
    l.append([' ']*c)
for i in range(r):
    for j in range(c):
        l[i][j]=input()
x,y=map(int,input().split())
for i in range(int(input())):
    s=input()
    if(s=='F'):
        if(x-1>=0 and l[x-1][y]!='X'):
            x-=1
        elif(x+1<r and l[x+1][y]!='X'):
            x+=1
        elif(y-1>=0 and l[x][y-1]!='X'):
            y-=1
        elif(y+1<c and l[x][y+1]!='X'):
            y+=1
print(x,y)