#
# This is the solution code for PyFlo Guided Project 1
#

# Ask the user for input values and convert to integers
width = input("Flag width:\n")
width = int(width)
height = input("Flag height:\n")
height = int(height)

# Calculate half of the width and height fur use in multiplication
half_width = int(width / 2)
half_height = int(height / 2)

# Create and print the rows of the flag
upper_row = '#' * half_width + '-' * half_width + '\n'
lower_row = '-' * width + '\n'
print(upper_row * half_height, end='')
print(lower_row * half_height, end='')