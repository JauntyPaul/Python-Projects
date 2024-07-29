# Second part of OOPS

# key word del for deleting the object or it's properties
# Eg: del s1.name or del s1

class Student:
    def __init__(self,name):
        self.name=name
        
        
s1=Student("Jonathan")
s2=Student("Ann")

print(s1.name,s2.name)

del s1             # Here the del command deletes the object s1


del s2.name  # Here the del command deletes the 'name' attribute/property of the object s2, the object is still present 


print(s2)    # This command line won't show an error but print(s2.name) will.


#####################################################################################

# Private methods

class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.acc_pass=acc_pass
        

acc1=Account("1234","abcde")

print(acc1.acc_no)

        
        
        