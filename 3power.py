n=int(input())
a=True
if(n%2==0):
    a=False
else :
    while(n%3==0):
        n/=3
    a=(n==1);
print(a)