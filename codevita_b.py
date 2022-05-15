c,n=map(int,input().split(" "))
seats=list(map(int,input().split(" ")))
info=[input().split(",") for i in range(n)]
dict={}
for i in info:
    dict[float(i[1])]=i[0]
percent=[]
for i in info:
    percent.append(float(i[1]))
percent=sorted(percent)
percent=percent[::-1]
print(percent)
for i in range(len(percent)):
    if(seats[0]>0):
        print(dict[percent[i]],info[i][2])
        seats[0]-=1
    elif(seats[1]>0):
        print(dict[percent[i]],info[i][3])
        seats[1]-=1
    elif(seats[2]>0):
        print(dict[percent[i]],info[i][4])
        seats[2]-=1
    n+=1