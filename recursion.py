# Recursion is the concept of calling a function within itself

def show(n):
    if n>0:    # Here n>0 is the base case where the recursion stops, generally this is where return case is shown
        print(n)
        show(n-1)

show(5)


print("\n")

# Factorial using recursion

def factorial(n):
    if (n==1 or n==0):
        return 1
    else:
        return n*factorial(n-1)
    
    
print(factorial(6))


print("\n")

# Recursive function to sum of n numbers.


def sum(n):
    total=0
    if(n>=0):
        total= total+n
        total+=sum(n-1)
    return total

print("The sum of numbers till 5 is",sum(5))




print("\n")


# Recursive function to print the elements in a list

list1 = [1,2,3,4,5,6,7]

def printer(list,num):
    if(num-1>=0):
        print(list[num-1])
        printer(list,num-1)
       
printer(list1,len(list1))  