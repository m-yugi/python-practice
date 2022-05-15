from typing import Dict


str="CodeHunt"
Dict={'a':'0','e':'1','i':'2','o':'3','u':'4'}
en="CodeHunt"
num=en[::-1]
for i in Dict:
    num=num.replace(i,Dict[i])
print(num)