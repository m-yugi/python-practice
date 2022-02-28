class adress_book:
    def __init__(self,book):
        self.book={}
    def addcontact(self,name,adress):
        if name in self.book:
            print("contact already exists")
        else:
            self.book[name]=adress
    def display(self):
        for u,v in self.book.items():
            print("name:{}  adress:{}".format(u,v))
    def disp_contact(self,name):
        if name not in self.book:
            print("the contact does not exists")
        else:
            print("this is the adress {} of the contact {}".format(name,self.book[name]))
    def delete(self,name):
        if name not  in self.book:
            print("the contact does not exist")
        else:
            del self.book[name]
            print("the contact is deleted")
class personal_adress(adress_book):
    def __init__(self,pres_book):
        self.pres_book=pres_book
    def addcontact(self,relation,adress):
        if relation in self.pres_book:
            print("contact already exists")
        else:
            self.pres_book[relation]=adress
    def display(self):
        for u,v in self.pres_book.items():
            print("name:{}  adress:{}".format(u,v))
    def disp_contact(self,relation):
        if relation not in self.pres_book:
            print("the contact does not exists")
        else:
            print("this is the adress {} of the contact {}".format(relation,self.book[relation]))
    def delete(self,relation):
        if relation not in self.pres_book:
            print("the contact does not exist")
        else:
            del self.pres_book[relation]
            print("the contact is deleted")
class office_adress(personal_adress):
    def __init__(self,office_book):
        self.office_book=office_book
    def addcontact(self,contact,adress):
        if contact in self.office_book:
            print("contact already exists")
        else:
            self.office_book[contact]=adress
    def display(self):
        for u,v in self.office_book.items():
            print("name:{}  adress:{}".format(u,v))
    def disp_contact(self,contact):
        if contact not in self.office_book:
            print("the contact does not exists")
        else:
            print("this is the adress {} of the contact {}".format(contact,self.book[contact]))
    def delete(self,contact):
        if contact not in self.office_book:
            print("the contact does not exist")
        else:
            del self.office_book[contact]
            print("the contact is deleted")
# def intro(flag,obj):
#     while(flag):
#         print("1.add contact 2.display book 3.display contact 4.delete 5.delete")
#         select=int(input())
#         if(select==1):
#             print("pls enter the  contact name")
#             name=input()
#             print("pls enter the adress")
#             adress=input()
#             obj.addcontact(name,adress)
#         elif select==2:
#             obj.display()
#         elif select==3:
#             print("pls enter the name of the contact")
#             con_name=input()
#             obj.disp_contact(con_name)
#         elif select==4:
#             print("pls enter the contact to be deleted")
#             delete=input()
#             obj.delete(delete)
#         elif select==5:
#             flag=False
# flag=True
# print("pls select the type")
# print("1.general  2.personal 3.office")
# intype=int(input())
# if(intype==1):
#     genral=adress_book({})
#     intro(flag,genral)
# elif(intype==2):
#     personal=personal_adress({})
#     intro(flag,personal)
# else:
#     office=office_adress({})
#     intro(flag,office)
genral=adress_book({})
genral.addcontact("sai","12345")
genral.addcontact("hello","56455")
genral.addcontact("hiii","85944")
genral.addcontact("mani","68395")
genral.disp_contact("sai")
genral.disp_contact("bala")
genral.disp_contact("hiii")
genral.display()
genral.delete("hello")
genral.delete("sai")
genral.display()
personal=adress_book({})
personal.addcontact("mom","12345")
personal.addcontact("dad","56455")
personal.addcontact("sis","85944")
personal.addcontact("uncle","68395")
personal.disp_contact("mom")
personal.disp_contact("bro")
personal.disp_contact("uncle")
personal.display()
personal.delete("mom")
personal.delete("bro")
personal.display()
office=adress_book({})
office.addcontact("f1","12345")
office.addcontact("f2","56455")
office.addcontact("f3","85944")
office.addcontact("f4","68395")
office.disp_contact("f1")
office.disp_contact("f10")
office.disp_contact("f2")
office.display()
office.delete("f1")
office.delete("f2")
office.display()