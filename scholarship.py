# class student:
#     def __init__(self,numb,email,name):
#         self.numb=numb
#         self.email=email
#         self.name=name
# class academic(student):
#     def __init__(self, numb,name , email,CGPA,AI):
#         super().__init__(numb, email,name)
#         self.cgpa=CGPA
#         self.ai=AI
#     def alot(self):
#         print(self.numb)
#         print(self.name)
#         if(self.cgpa=='S' and self.ai<=30000):
#             print(0.0)
#         elif self.cgpa=='A' and (self.ai>=31000 and self.ai<=100000):
#             print(100000.0)
#         else:
#             print(200000.0)
# class sports(student):
#     def __init__(self, numb, name , email,level,numb_games):
#         super().__init__(numb, email,name)
#         self.level=level
#         self.numb_games=numb_games
#     def alot(self):
#         print(self.numb)
#         print(self.name)
#         if(self.level=="international" and self.numb_games>=2):
#             print(0.0)
#         elif self.level=="national" and (self.numb_games>=5 and self.numb_games<=10):
#             print(100000)
#         elif(self.level=="state" and (self.numb_games>=20 and self.numb_games<=30)):
#             print(150000)
#         else:
#             print(200000)
# print("please select an option")
# n=int(input("1. academics\n2.sports \n"))
# if(n==1):
#     pub=int(input("please enter the registration number\n"))
#     des=input("please enter your email\n")
#     name=input("please enter your name\n")
#     pro=(input("please enter your CGPA \n"))
#     code=int(input("please enter your annual income\n"))
#     teacher=academic(pub,name,des,pro,code)
#     teacher.alot()
# else:
#     pub=int(input("please enter the registration number\n"))
#     des=input("please enter your email\n")
#     name=input("plesae enter your name\n")
#     pro=(input("please enter your level\n"))
#     code=int(input("please enter total no of games played\n"))
#     trainer=sports(pub,name,des,pro,code)
#     trainer.alot()
l=[i for i in range(5) if(i%2==0)]
print(l)