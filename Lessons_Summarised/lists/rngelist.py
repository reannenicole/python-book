# You can use the range() function to generate a lit of numbers 
# remember this prits _between_ 1-10, so doesn't print 10

for value in range(1,10):
    print(value)

#using this fucntion, you can create a list of numbers: 
    
numbers = list(range(1,10))
print(numbers)

# We can also use the range() function to tell Python to skip numbers in a range
# For example: 
# the range() function starts with the value 2 and then add 2 repeatadly until it reaches the last value

even_numbers = list(range(2,11,2))
print(even_numbers)

# And you can use this for multiples!!

multiples_four = list(range(4,50,4))
print(multiples_four)

# range() can be used to create many sets f numbers, like squares
# the below times each number in the list by itself, creating the first 10 square numbers

squares = []
for value in range(1,11):
   square = value**2
   squares.append(square)

print(squares)

# this can be used on a data set of any size!

more_squares = []
for value in range(1,100):
    more_square = value**2
    more_squares.append(more_square)

print(more_squares)

# this is where we get to statistics!!!

