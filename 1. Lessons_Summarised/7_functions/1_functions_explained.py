# a function is a written block of code
# that is designed to do a task 
# writing one into your programme means that
# you can call it indefinitley. 

# this means your code is more concise, as you don't
# have to type out the cod eover and over. 

# here's a simple example: 

def greet_user(): 
    """Display a simple greeting"""
    print("Hello!")

greet_user()

# this is a basic function that just prints "hello" when called
# def inform python that you are creating a function 
# after this is the name of the function 
# and anthing indented is the body of the function 

# so, putting this all together, we have created a function 
# called greet_user that prints hello when called

# so to expand on this, and make a useful function, we need to 
# pass information through it!

def greet_user2(username):
    print("Hello, " + username.title())

greet_user2("reanne")

# as we see in this second function "greet_user2"
# you are telling the function to accept the value of "username"
# so when you call the function, you pass it a name to work with

