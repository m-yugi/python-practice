from pickletools import markobject


marklist={}
failed=[]
centi=[]
for i in range(int(input("enter number of students"))):
    regnum=int(input("Enter first student register number"))
    engmark=int(input("Enter first student English marks"))
    mathmark=int(input("Enter first student Mathematics mark"))
    scimark=int(input("Enter first student Science mark"))
    if(engmark>50 or mathmark>50 or scimark>50):
        failed.append(regnum)
    if(mathmark==100):
        centi.append(regnum)
    marklist[regnum]=engmark+mathmark+scimark
if(marklist):
    print(marklist.get(max(marklist,key=marklist.get())))
else:
    print("NA")
if(failed):
    for i in failed:
        print(i)
else:
    print("NA")
if(centi):
    for i in centi:
        print(i)
else:
    print("NA")

