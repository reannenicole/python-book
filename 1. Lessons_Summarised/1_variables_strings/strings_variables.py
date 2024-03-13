# A string is a series of character, defined by "" or '' 

print("So this here would be a string!")

# A variable is like a label that you a assign a value!
# variable names can only include normal characters, with the exception of an underscore
# which is used instead of a space!
# You should also avoid using function names and keywords, as Python might get confused :(

message = ("Hello future Reanne!")
print(message)

# you can add another line to a variable at any point during your code!

message = ("Hello past Reanne!")
print (message)

#After a string is written, you can manipulate the data within it with different methods
# Such as below, where if we say something is a "title", it will capitalise the first letter

name = "reanne"
print(name)
print(name.title())

# Heres some other things you can do!

print(name.upper())
print(name.lower())

# Combining what we have learnt, you can use a variable within a string! 
# Say you've had someone input their name and you want to great them: 
# The below contains something called an f string, f meaning format
# Thisformats the string by replacing the variable name with its string value!

first_name = ("reanne")
last_name = ("pearce")

full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

# There is also a method to add whitespace, which makes output more readable!
# \t adds a tab 

print("python")
print("\tpython")

# To add a new line its \n 

print("Languages:\npython\nrust\njavascript")

# Or combine the two to make a nice looking list

print("Languages:\n\tpython\n\trust\n\tjavascript")

# But what if you have whitespace that you don't need? Lets say you're colating user added data,
# 10 people have answered the question in the same way but added a space at the end
# Python will take these as two seperate values, which will end up in mistakes with your data!

favourite_language = " python "
favourite_language.lstrip
print(favourite_language)


