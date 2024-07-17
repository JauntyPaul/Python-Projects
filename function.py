# Functions in Python


def cal_sum(a, b):
    sum = a+b
    print(sum)
    return sum
s=5
t=9
cal_sum(s,t)

print('\n')

# Using the returning of a function

def read():
    name = input("Enter you name ")
    return name

string = read()
print("Welcome",string)


print("\n")
# functions which does not have a return value, returns a None value

# WAP to generate a function that prints the avg of 3 no.
def avg(a,b,c):
    result=(a+b+c)/3
    print(result)
   
avg(4,5,6)    

print("\n")
# Assigning default values for parameters,so that the function runs, even if the function is called withtout parameters 

def cal_mul(a=1,b=1):  # When assigning default parameters, always start assign from right, Eg: cal_mul(a,b=2)
    print(a*b)
    return a*b

cal_mul() # This function will print 1 since there are no paramters
cal_mul(5) # This function will print 5 since there are is only 1 paramter and other is considered one by default.


print("\n")


# End of a print function

print("Hello",end=" ") # Default end is assigned to "\n", replacing that replaces the parameter of function,
print("friend")        # and the output changes, in this case the next output was print on the same line.