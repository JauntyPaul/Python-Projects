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
        self.acc_pass=acc_pass # Here the acc_pass is public, which makes it accesible outside the class 
        self.__acc_pass=acc_pass # Adding 2 underscore make the attribute private to the class
        

acc1=Account("1234","abcde")

print(acc1.acc_no)
print(acc1.acc_pass) # Here the acc_pass will be printed
                     # But if this was __acc_pass it would show an error
        
# But if this same __acc_pass is called within the class, it can be used.
# Eg:   
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass
         
    def reset_pass(self):
        print(self.__acc_pass) # This function will be able to call the private attribute 
        
acc2=Account("1426","Shibu Dinam")
acc2.reset_pass()


print ("\n")          
##############################################################################

class Person:
    __name ="anonymous" # Here this is name is not public, can't be printed called outside the class
    
    def __hello(self,name):
        print("Hello person") # Calling this function outside the class with object will give an error
        
    def welcome(self):
        self.__hello(self)
        
p1=Person()

p1.welcome()