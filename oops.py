# Obeject Oriented Programing 

class Student:
    nane="Jaunty"
    def __init__(self): # Here is the init is the constructor which we have created and we don't do it, \n
        print(self)     # Python does it, also for init we always have to pass the attribute self, \n
        print("Inside the function")    # We can rename self to whatever name we want, for eg: __init__(abcd)
    
    
s1 = Student()  # Here s1 is an object from class Student
print(s1)
 
print("\n")
######################################################### 
        
class Student2:
    def __init__(self,name):   # name is the attribute, These Constructors are parameterized 
        self.name = name         #value of name is assigned to the the self.name
        print("The name is being printed")
        
        
s2=Student2("Alex")
print(s2.name)
s3=Student2("Mathew")
print(s3.name)

print("\n")
###################################################


class Student3:
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark
        
s4=Student3("John",87)
print(s4.name,s4.mark)
        