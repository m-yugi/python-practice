def genrator(num):
    l=[]
    for i in range(0,len(num),2):
        c=pow(num[i],3)
        l.append(c)
    return l
x=[1,2,3,4,5,6]
l=genrator(x)
for i in l:
    print(i)