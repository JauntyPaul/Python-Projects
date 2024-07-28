#Practice question for OOPS

# Create a class called Account, wiht atrr balance and account no., also create methods debit, credit, and balance

class Account:
    def __init__(self,accNo,bal):
        self.bal = bal
        self.accNo = accNo
    
    def debit(self,amount):
        self.bal=self.bal-amount
        print("Rs.",amount,"has been Debited")
        print("The Balance:",self.bal)
        
    def credit(self,amount):
        self.bal=self.bal+amount
        print("Rs.",amount,"has been Credited")
        print("The Balance:",self.bal)
        
    def balance(self):
        print ("Balance amount:",self.bal)
        
  
  
ac1=Account(101,50000)   
ac1.credit(100)
ac1.debit(20000)
ac1.balance()