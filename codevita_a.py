n=int(input())
power=list(map(int,input().split(" ")))
cap=[]
iron=[]
end=len(power)-1
for i in range(len(power)):
    if(power[i]>0):
        if(power[i] not in iron):
            cap.append(power[i])
    else:
        