plants=[1,2,4,4,5]
count=0
capa=6
capb=5
can1=capa
can2=capb
b=len(plants)-1
a=0
while(a<b):
    if(can1<plants[a]):
        count+=1
        can1=capa
        can1-=plants[a]
    else:
        can1-=plants[a]

    if(can2<plants[b]):
        count+=1
        can2=capb
        can2-=plants[b]
    else:
        can2-=plants[b]
    b-=1;
if(len(plants)%2!=0):
    maxi=max(can1,can2)
    if(maxi<plants[a]):
        count+=1
print(count)