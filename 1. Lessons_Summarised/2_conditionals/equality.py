# an if statement is basically just checking if what you have asked is True or False
# and we can use this to execute a function based on the answer.

colour = "Red"
print(colour == "Red")
print(colour == "Blue")

#this process is case sensitive in python
# meaning that it is best to covert the string to one case before executing
# it doesn't change the original value, just what the fucntion looks for

print(colour == "red")
print(colour.lower() == "red")

# you can also use python to check for inequality

print("What order are you making next?")
order_1 = "sandwich"
order_2 = "burger"
if order_1 != order_2:
    print("That's for the wrong customer!")
