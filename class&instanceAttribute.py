# Attribute of Class and it's instances

class College: 
    college_name= "Apna College"    # Common attributes are called class attributes
    name="Parayulla"
    def __init__(self,name):
        self.name= name                # Each person has different name, thus instance attribute is used.
        
s1=College
print(s1.college_name) # Can be also written as Student.college_name

s2=College("Sam")
print(s2.name)      # We need to call the instance name to get the name     #obj.attr
print(College.name) #class.attr
        