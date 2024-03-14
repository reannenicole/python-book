# the input function allows user submitted information to be a part of your code
# to do this, we must simply use input() around a prompt

message = input("how was your day today? ")
if message == "good":
    print("I'm glad to hear it!")
elif message == "bad": 
    print("i'm sorry to hear that!")
elif message == "okay": 
    print("I hope it gets a little better")
else:
    print("sorry i didn't understand, tell me again how your day was!")

# by default, everything input by the user will be registered as a string, but we can change this 
# by making this into an int rather than a string, we can then enter them into functions 
    
current_year = int(input('what year is it? '))
received_year = int(input('What year did you get your passport? '))
if received_year + 10 < current_year:
    print('You should go get a new passport!')
if received_year + 10 == current_year:
    print('You should get a new passport sometime soon')
if received_year + 10 > current_year:
    print('You do not need to get a new passport for now')