# a while loop iin python functions similarly to a for loop 
# but whilst a for loops executes once 
# a while loop will continue executing code -while- the boolean condition continues to be true 

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# with a while loop, you can let a user decide when the program quits
    
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
print(message)
