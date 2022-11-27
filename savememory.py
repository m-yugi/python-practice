s = []
k = 2
max_sum = 9223372036854775807
sumi = 0
if(k == 0):
    print(sum(s))
if not s:
    print(0)
for i in range(len(s)):
    if(i+k <= len(s)):
        sumi = sum(s[:i]+s[i+k::])
        if(max_sum > sumi):
            max_sum = sumi
print(max_sum)
