for i in range(int(input())):
    w,x,y,z=map(int,input().split(" "))
    if(w+(y*z)==x): print("filled")
    elif(w+(y*z)>x): print("overFlow")
    else: print("Unfilled")