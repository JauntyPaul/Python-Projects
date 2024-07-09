# WAP to read 3 names of movie from the user and store it in list

movie1 = input("Enter the name of Movie 1\n")
movie2 = input("Enter the name of Movie 2\n")
movie3 = input("Enter the name of Movie 3\n")
list = [movie1,movie2,movie3]
print(list)

# WAP to check whether the list contains palindrome of elements

list1 = [2,121,121,2]
copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("Palindrome elements")
else:
    print("Not Palindrome elements")