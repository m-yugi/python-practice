d={'2':"abc",'3':"def",'4':"ghi",'5':"jki",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
n=input()
var=[]
m=[]
if len(n)==1:
    for i in d[n]:
        m.append(i)
elif len(n)==0:
    pass
else:
    for i in n:
        var.append(d[i])