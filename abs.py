import sys
s1 = "1010"
s2 = "1011"
if s1=="0" and s2=="0":
    print(0)
elif s1 and s2=="0":
    print(s1)
elif s1==0 and s2:
    print(s2)
carry=0
output=""
a=len(s1)-1
b=len(s2)-1
maxlen=max(len(s1),len(s2))
while maxlen>0:
    x=int(s1[a]) if a>=0 else 0
    y=int(s2[b]) if b>=0 else 0
    k=x+y+carry
    if k==1:
        carry=0
    elif k==2:
        k=0
        carry=1
    elif k==3:
        k=1
        carry=1
    output+=str(k)
    a-=1
    b-=1
    maxlen-=1
if carry:
    output+=str(carry)
print(output[::-1])