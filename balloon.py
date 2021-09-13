text="loonbalxballpoon"
d = {'b':0, 'a':0, 'l':0, 'o':0, 'n':0}  
for ch in text:
    if ch in d:
        d[ch] += 1 if ch in ('l', 'o') else 2
print(min(d.values()) // 2)