# slicing is all about working with a specific group of items containted within a list
# for example below, we have a list of 7 names, but only want to work with the first 3!

milk_types = ["normal", "chocolate", "strawberry", "banana", "vanilla"]
print(milk_types[0:3])

# this can be done with any range of number that's in the list

print(milk_types[2:4])

# and using no parameter at the start or the end will give you everthing from or to that place
# meaning you can pull all entries from the list from a certain point onward, no matter if you know
#the length or not!

print(milk_types[1:])
print(milk_types[:3])

# you can even use the negative index!

print(milk_types[-4:])

# expanding on this concept, a slice will function as a normal list, so can be used with other 
# functions such as for loops

print("Here is a short list of some of the types of milk we sell in this store: ")
for milks in milk_types[:3]:
    print(milks.title())

