import calendar
def insane(bday,bmon,byear,cday,cmon,cyear):
    if(bmon>cmon):
        print("take my sanity",cyear-byear-1)
    elif(bmon<cmon):
        print("pls take my sanity",cyear-byear)
    else:
        if(bday>cday):
            print("i dont want this saniry anymore",cyear-byear)
        elif(bday<=cday):
            print("i will go die",cyear-byear)
bday,bmon,byear=map(int,input().split("/"))
cday,cmon,cyear=map(int,input().split("/"))
if calendar.isleap(byear):
    if(bmon==2):
        if(bday==29):
            print("the age is",cyear-byear)
    else:
        insane(bday,bmon,byear,cday,cmon,cyear)
else:
    insane(bday,bmon,byear,cday,cmon,cyear)