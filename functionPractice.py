# Function Practice Problems

# Function to print the length of the list
list1 = [1,2,3,4,5]
def listlen(list):
    length = len(list)
    print(length)
    return length

listlen(list1)

print("\n")

# Function to print the elements of a list in a single line

def printlist(list):
    i=0
    for i in list:
        print(i,end=" ")
        i+=1
    
printlist(list1)


print("\n")


# Function to find the factorial of number n

def factorial(n):
    fact=1
    i=1
    while i<=n:
        fact*=i
        i+=1
    print(fact)
    
factorial(5)