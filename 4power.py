import math
n=int(input())
a=True
if(n==0):
    a=False
else:
    m=math.ceil(math.log10(n)/math.log10(4))
    c=math.floor(math.log10(n)/math.log10(4))
    a=(m==c);
print(a)