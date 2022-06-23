import sys
import os
lh,lm=map(int,input().split())
th,tm=map(int,input().split())
ah=lh+th
am=lm+tm
while(am>=60):
    ah+=1
    am-=60
if(ah==24):
    ah=0
elif(ah>24):
    ah-=24
print(f"{ah:02d}", f"{am:02d}")