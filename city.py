from calendar import month
from operator import le
from traceback import print_tb


l=[2,1,9,3,1,4]
num=3
month=6
sum=0
res=[]
for i in range(len(l)//num):
    res.append(l[sum:sum+num])
    sum+=num
for i in res:
    i.sort()
for i in range(len(res)):
    if(res[i[0]]):
