def wrap(s, w):
    l=[]
    count=0
    prev=0
    n=0
    while(n<len(s)):
        if(count!=w):
            count+=1
            n+=1
        else:
            l.append(s[prev:n])
            prev=n
            count=0
    l.append(s[prev:len(s)])
    return "\n".join(l)
string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)