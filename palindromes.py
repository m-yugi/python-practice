d={'a':2,'b':2,'c':2,'d':3,'e':3,'f':3,'g':4,'h':4,'i':4,'j':5,'k':5,'l':5,'m':6,'n':6,'o':6,'p':7,'r':7,'s':7,'t':8,'u':8,'v':8,'w':9,'x':9,'y':9}
l=[]
d1={}
for i in range(int(input())):
    l.append(input())
for i in l:
    m=""
    for j in i:
        if(j.isdigit()):
            m+=j
        elif(j=='-'):
            pass
        else:
            m+=d(j.lower())
    d1[m]=1
print(d1)