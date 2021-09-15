word="Leetcode"
n=len(word)
b=True
if(n==1):
    print(b)

if(word[0].isupper() and word[0].isupper()):
    for i in range(2,n):
        if not word[i].isupper():
            b=False
else:
    for i in range(1,n):
        if(word[i].isupper()):
            b=False
print(b)