x=4
y=7
if(x>y):
    gn=x
else:
    gn=y
while(True):
    if(gn%x==0 and gn%y==0):
        ans=gn
        break
    else:
        gn+=1
print(ans)