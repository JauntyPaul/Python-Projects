# Python Loop practice Problems

# Print numbers from 1 to 100.

i = 1
while i<=100:
    print(i)
    i+=1

print("\n")
# Print numbers from 100 to 1.

i = 100
while i>=1:
    print(i)
    i-=1

print("\n")
# Print the multiplication table of a number n.

n =int(input("Enter a number "))
i=1
while i<=10:
    print(i*n)
    i+=1

print("\n")
# Print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
i=0
while i<=9:
    print(list[i])
    i+=1

print("\n")
# Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
x = int(input("Enter the value of x "))

i=0
while i<len(tup):               # here condition could have also been i <= len(tup)-1
    if (tup[i]==x):
        print("Found",x,"at index ",i)
        i+=1
    else:
        print("searching..")
        i+=1
print("Searching Complete")

print("\n")
# Concept of Break & Continue 

#BREAK
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
x = int(input("Enter the value of x "))
i=0
while i<len(tup):               # here condition could have also been i <= len(tup)-1
    if (tup[i]==x):
        print("Found",x,"at index ",i)
        i+=1
        break                  # Code after break is not executed
    else:
        print("searching..")
        i+=1
print("Searching Complete")

print("\n")
#CONTINUE
i=1
while i<=5:
    if(i==3):
        i+=1
        continue #Code resume from next interation, skips the part after continue
    print(i)
    i+=1