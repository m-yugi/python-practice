x=int(input())
y=int(input())
count=0
s=x^y
s=str(format(s,"b"))
for i in s:
    if i=='1':
        count+=1
print(count)