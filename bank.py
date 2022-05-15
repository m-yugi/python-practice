class bank:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,depo):
        self.balance+=depo
    def withdraw(self,withdraw):
        if(self.balance>withdraw):
            self.balance-=withdraw
        else:
            print("insufficent balance")
    def display(self):
        print(int(self.balance))
class intrest(bank):
    def __init__(self, balance,intrest):
        super().__init__(balance)
        self.intrest=intrest
    def deposit(self, depo):
        self.balance+=depo
        self.balance+=(self.intrest)*self.balance
    def withdraw(self, withdraw):
        return super().withdraw(withdraw)
    def display(self):
        return super().display()
class charging(bank):
    def __init__(self, balance,fee):
        super().__init__(balance)
        self.fee=fee
    def deposit(self, depo):
        return super().deposit(depo)
    def withdraw(self, withdraw):
        if(self.balance>withdraw):
            self.balance-=withdraw+self.fee
        else:
            print("insufficent balance")
    def display(self):
        return super().display()
acc=int(input())
if(acc==1):
    bal=int(input())
    s=intrest(bal,0.15)
    depo=int(input())
    s.deposit(depo)
    withd=(int(input()))
    s.withdraw(withd)
    s.display()
elif(acc==2):
    bal=int(input())
    s=charging(bal,10)
    depo=int(input())
    s.deposit(depo)
    withd=(int(input()))
    s.withdraw(withd)
    s.display()
else:
    print("Account Type Does Not Exist")