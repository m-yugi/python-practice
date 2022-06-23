for i in range(int(input())):
    x,y=map(int,input().split())
    count=0
    while(1):
        if(x>=y):
            break
        else:
            count+=1
            x+=8
    print(count)