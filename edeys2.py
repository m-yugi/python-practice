s=input()
x,y=map(int,s[0:3].split())
print(x)
l=list(map(int,s[4::].split()))
l1=[]
alp="abcdefghijklmnopqrstuvwxyz"
s=''
s1=''
for i in range(0,len(l),x):
    l1.append(l[i:i+x])
for j in range(x-1,-1,-2):
    y-=1
    print(y,j)
    print(l1[j-1][y])
    s+=alp[((l1[j][y])%26)-1]
    s1+=alp[(l1[j][y-j]%26)-1]
s+=s1[:len(s1)-1]
s=s[::-1]
print(s)
# 7 7 26 28 5 18 27 32 50 13 42 32 11 5 40 27 16 34 23 49 44 17 36 48 10 46 20 13 43 36 1 10 19 29 23 22 20 49 35 15 41 7 29 34