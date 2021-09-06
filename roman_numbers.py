s=input("enter the roman value")
ref={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
num=0
n=len(s)
while(n>0):
    e=n-1
    if(e!=0 and ref.get(s[e])>ref.get(s[e-1])):
        num+=(ref.get(s[e])-ref.get(s[e-1]))
        n-=2
    else:
        num+=ref.get(s[e])
        n-=1
print(num)