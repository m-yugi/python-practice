def deletecontact(name, phonebook):
    del phonebook[name]
def addcontact(phonebook):
    if not phonebook:
        print("\npls enter the name and number of the contact\n")
        a=input()
        phonebook[a]=int(input())
    else:
        print("\npls enter the name of the contact\n")
        x=input()
        if x in phonebook:
            print("\nsorry the contact already exists\n")
        else:
            print("\npls enter the number of contact\n")
            phonebook[x]=int(input())
def display(phonebook):
    for i in sorted(phonebook.keys(
        
    )):
        print(i," ",phonebook[i])
phonebook={}
flag=True
while(flag):
    print("\n1.add contact\n2.delete contact\n3.display\n4.exit\n")
    s=input()
    if(s=="1"):
        addcontact(phonebook)
    elif(s=="2"):
        if not phonebook:
            print("\nthe phonebook is empty\n")
        print("\npls enter the name of contact to be deleted\n")
        deletecontact(input(),phonebook)
    elif(s=="3"):
        display(phonebook)
    elif(s=="4"):
        flag=False
