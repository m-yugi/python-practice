s=input()
count4=0
count7=0
m=True
if '4' not in s or '7' not in s:
    print(-1)
else:
    for i in s:
        if i=='4':
            count4+=1
        elif i=='7':
            count7+=1
if(count7==count4):
    print(4)
elif(max(count4,count7)=='4'):
    print(4)
else:
    print(7)