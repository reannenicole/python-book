# When a list is made from user submitted or found values, they can be in an unpreicatable order!
# In Python, theres a lot of different ways of sorting these lists!

# With the sort() method, we can pemanently alter the list to in an alphabetical order!

favourite_movies = ["LOTR", "Dune", "Hackers", "Swordfish", "Clerks"]
favourite_movies.sort()
print(favourite_movies)

# Or reverse alphabetical order!

favourite_movies.sort(reverse=True)
print (favourite_movies)

# To present the list in a sorted order, but maintain the original format, we use sorted()

next_gen = ["Picard", "Riker", "Data", "Deanna", "Worf"]

print("Here are my favourite characters from TNG in no particular order:")
print(next_gen)

print("\nand here they are in alphabetical order: ")
print(sorted(next_gen))

# Reverse()

print("\nand here they are reversed!: ")
next_gen.reverse()
print(next_gen)

# Reverse() Permanently alters the order, but can be changed back using the reverse function again!

print("\n ...and back to the original")
next_gen.reverse()
print(next_gen)
