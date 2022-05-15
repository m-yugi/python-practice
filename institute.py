class staff:
    def __init__(self,code_name):
        self.code_name=code_name
class faculty(staff):
    def __init__(self,designation,publications,projects,code_name):
        self.designation=designation
        self.publications=publications
        self.projects=projects
        super().__init__(code_name)
    def promotion(self):
        if(self.publications>=10):
            print()
            print(self.code_name)
            print(self.designation)
            print("promoted")
        elif(self.publications>=5 and self.projects>=1):
            print()
            print(self.code_name)
            print(self.designation) 
            print("promoted")
class officer(staff):
    def __init__(self,grades,experiance,code_name):
        self.grades=grades
        self.experiance=experiance
        super().__init__(code_name)
    def promotion(self):
        if(self.experiance>10):
            print()
            print(self.code_name)
            print(self.grades)
            print("promoted")

print("1. faculty\n2.officer \n")
n=int(input("Enter the type of staff :"))
print()
if(n==1):
    code=input("please enter code for the staff : ")
    print()
    des=input("please enter the designation of the faculty :")
    print()
    pub=int(input("please enter the total no of publications by faculty :"))
    print()
    pro=int(input("please enter the total no of projects by faculty :"))
    teacher=faculty(des,pub,pro,code)
    teacher.promotion()
else:
    pub=int(input("please enter the grade of the officer :"))
    print()
    pro=int(input("please enter the experince of the officer : "))
    print()
    code=input("please enter code for the officer: ")
    trainer=officer(pub,pro,code)
    trainer.promotion()