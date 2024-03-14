# in a long and complicate program, you may need to "flag" your while loops/ 
# For a program that should run only as long as many conditions are true,
# you can define one variable that determines whether or not the entire program is active.
# this flag then sends a signal to the program based on whether the flag value is True or False
# all other tests then fit neatly in 

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
