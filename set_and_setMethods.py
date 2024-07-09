# Set datastructure in Python

collection = {1,2,3,4}
print(collection)
print(type(collection))

print("\n")

emptyset = {}           # This is the syntax for empty dictionary so we use a different method of representation
print(type(emptyset))
emptyset = set()        # This is the sytanx for empty set
print(type(emptyset))
print(emptyset)

print("\n")

# Methods used in set

print("Methods used with set\n")
collection.add(5)   # used to add new element
print(collection)

collection.remove(3) # used to remove a existing element, would give an error if the value does not exist
print(collection)

collection.pop()    # used to remove random element
print(collection)

collection.clear()  #empties the entire set, returns empty set on print 
print(collection)

print("\nMethods Union and Intersection\n")

set1 = {1,2,3}
set2 = {3,4,5}
print(set1.union(set2))         # used to find the union
print(set1.intersection(set2))  #used to find the intersection

print("\nUnion and Intersection does not change the initial values\n")

print(set1)     #using union or intersection does not change the original sets
print(set2)
