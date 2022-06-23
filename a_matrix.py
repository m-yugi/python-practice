import math
from operator import le
def Add(a,b):
    c=[[0]*len(a)]*len(a)
    for i in range(0,len(a)):
        for j in range(0,len(a)):
            c[i][j] = a[i][j] + b[i][j]
    return c
def Mul(a,b):
    c=[[0]*len(a)]*len(a)
    for i in range(0,len(a)):
        for j in range(0,len(a)):
            for k in range(0,len(a)):
                c[i][j]+= a[i][k] * b[k][j]
        return c
def Sub(a,b):
    c=[[0]*len(a)]*len(a)
    for i in range(0,len(a)):
        for j in range(0,len(a)):
            c[i][j] = a[i][j] - b[i][j]
        return c
n=int(math.sqrt(int(input())))
a=[]
b=[]
for i in range(n):
    a.append(list(map(int,input().split())))
for j in range(n):
    b.append(list(map(int,input().split())))
print("Sum")
c=Add(a,b)
for i in range(n):
    for j in range(n):
        print(c[i][j], end=" ")
    print()
print("Difference")
c=Sub(a,b)
for i in range(n):
    for j in range(n):
        print(c[i][j], end=" ")
    print()
print("Multiply")
c=Mul(a,b)
for i in range(n):
    for j in range(n):
        print(c[i][j], end=" ")
    print()