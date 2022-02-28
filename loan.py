class Loan:
    def __init__(self,principal,term,rate):
        self.principal=principal
        self.term=term
        self.rate=rate
    def getMonthlyPayment(self):
        return self.principal*self.rate*self.term
class mortgage(Loan):
    def __init__(self, principal, term, rate):
        super().__init__(principal, term, rate)
    def __init__(self,adress,propertyTaxRate):
        self.adress=adress
        self.propertTaxRate=propertyTaxRate
    def calculatePropertyTax(self):
        return self.propertTaxRate
class carloan(Loan):
    def __init__(self, principal, term, rate):
        super().__init__(principal, term, rate)
    def __init__(self,bankFee,make,model):
        self.bankFee=bankFee
        self.make=make
        self.model=model
l=Loan(10000,10,5)
n=mortgage(12345,40)
c=carloan
print(l.getMonthlyPayment())
print(n.calculatePropertyTax())