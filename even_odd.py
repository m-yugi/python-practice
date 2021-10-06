s="anagram"
t="nagarm"
d={}
d2={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d.update({i:1})
for i in t:
    if i in d2:
        d2[i]+=1
    else:
        d2.update({i:1})
print(d)
print(d2)