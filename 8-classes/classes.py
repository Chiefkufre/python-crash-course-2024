


class BankAccount:
    def __init__(self, customeName, bankName):
        self.customerName = customeName
        self.bankName = bankName
        self.charges = 30
        self.actBalance = 0.0


    def depositFund(self, amt):
         self.actBalance = amt + self.actBalance
         return self.actBalance
    
    def withDrawFund(self, amt):
        self.actBalance = self.actBalance - (amt + self.charges)
        return self.actBalance
    
    def balance(self):
        return self.actBalance
    
    def accountName(self):
        return self.customerName



samuel = BankAccount("samuel", "Firstbank")

print(samuel.balance())

samuel.depositFund(5000)

print(samuel.balance())

samuel.withDrawFund(3000)

print(samuel.balance())
