s=input()
count=0
i=0
if(len(s)<4):
    print(0)
else:
    while(i<len(s)):
        if(i+2<len(s) and i+3<len(s)):
            if(s[i:i+2]+'g'+s[i+3]=='doge'):
                count+=1
                i+=4
            else:
                i+=1
        else:
            i+=1
    print(count)