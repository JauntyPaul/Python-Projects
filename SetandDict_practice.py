# Practice questions from Set and Dictionary

# Q1.To store following word meaning in a Dictionary

dict1={
    "table":("a piece of furniture","list of facts and figures"),
    "cat":"a small animal"
}
print(dict1)
print("\n")

# Q2. You are given a list of subjects for students. Assume one classroom is required for 1 subject. \n
# How many classrooms are needed by all students.

subjects = {"python","java","C++","python","javascript","java","python","java","C++","C"}
num = len(subjects)
print("Number of classes required = ",(num))
print("\n")

# Q3.WAP to enter marks of 3 subjects from the user and store them in a dictionary. 
# Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

dict2 = {}
mark1 = int(input("Enter the marks in Maths"))
dict2.update({"Maths":mark1})
mark2 = int(input("Enter the marks in Phy"))
dict2.update({"Phy":mark2})
mark3 = int(input("Enter the marks in Chem"))
dict2.update({"Chem":mark3})
print(dict2)

# Q4.Figure out a way to store 9 & 9.0 as separate values in the set. (You can take help of built-in data types)

set1={9,(9.0,)} # There are multiple options
set1={9,"9.0"}
set1={"9",9.0}
print(len(set1))