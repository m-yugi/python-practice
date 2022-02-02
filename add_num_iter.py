arr=[1,2,3,4]
lis=[]
l=len(arr)
for i in range(1,l+1):
    for k in range((l-i)+1):
        s=""
        for j in range(k,i+k):
            s+=str(arr[j])
        if(s!=""):
            lis.append(int(s))
print(lis)