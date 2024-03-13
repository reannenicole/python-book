# say you want to create a list that cannot be changed, we would use "tuples" whic create 
#immutable lists
#A tuple looks just like a list except you use parentheses instead of square
#brackets. Once you define a tuple, you can access individual elements by
#using each item’s index, just as you would for a list.

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# the syntax for lists and tuples is the same, and we can use them for the same fuctions!

dimensions = (200, 50)
for dimension in dimensions:
 print(dimension)

# Although you can’t modify a tuple, you can assign a new value to a variable
# that holds a tuple.
 
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
 print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
 print(dimension)