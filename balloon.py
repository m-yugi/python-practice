a=0 
b=0
l=0
o=0
n=0
#works for any input
s="bollonoa"
for i in s:
    if i=='b': b += 1
    elif i=='a': a += 1
    elif i=='l': l += 1
    elif i=='o': o += 1
    elif i=='n': n += 1
l=l//2
o=o//2
print(min(b,min(a,min(l,min(o,n)))))