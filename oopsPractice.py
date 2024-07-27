#Practice question for OOPS

# Create a class called Account, wiht atrr balance and account no., also create methods debit, credit, and balance

class Account:
    def __init__(self,accNo,bal):
        self.balance = bal
        self.accNo = accNo
    
    def debit(self,amount):
        self.balance=self.balance-amount
        
    def credit(self,amount):
        self.balance=self.balance+amount
        print("hello 100 bucks")
        
    def balance(self):
        return self.balance
  
  
ac1=Account(101,50000)   
ac1.credit(100)
