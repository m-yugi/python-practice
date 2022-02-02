d1={"5":5,"9":9,"11":11,"20":20,"4":4}
d2={"6":6,"5":5,"9":9,"4":4,"21":21}
m={}
for i in d1:
    if i in d2:
        m[i]=d1[i]+d2[i]
    else:
        m[i]=d1[i]
for j in d2:
    if j not in m:
        m[j]=d2[j]
for key,value in m.items():
    print(key,value)