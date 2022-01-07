l=[1,3,3]
sum=0
wind=1;
while(wind!=len(l)):
    for i in range(len(l)):
        l2=[l[i] for i in range(i+wind)]
        print(l2)
    wind+=1