from pickletools import markobject


marklist={}
failed=[]
centi=[]
for i in range(int(input("enter number of students"))):
    regnum=input("Enter first student register number")
    engmark=int(input("Enter first student English marks"))
    mathmark=int(input("Enter first student Mathematics mark"))
    scimark=int(input("Enter first student Science mark"))
    if(engmark<50 or mathmark<50 or scimark<50):
        failed.append(regnum)
    else:
        failed.append(0)
    if(mathmark==100):
        centi.append(regnum)
    else:
        centi.append(0)
    marklist[regnum]=engmark+mathmark+scimark
if(marklist):
    maxi=max(marklist,key=marklist.get)
    maxii=[]
    for key,value in marklist.items():
        if(marklist[maxi]<=value):
            maxii.append(key)
    for i in maxii:
        print(i)
    print()
else:
    print("NA") 
    print()
if(centi):
    for i in centi:
        if(i!=0):
            print(i)
        else:
            print("NA")
else:
    print("NA")
print()
if(failed):
    for i in failed:
        if(i!=0):
            print(i)
        else:
            print("NA")
else:
    print("NA")
print()