# to exit out of a while statement, we need to use the break statement
# this is mean code is only executed as and when it is necessary 
# a loop that starts with a while statement will run forever unless accompanies by a break 

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)
    if city == 'quit':
       break
    else:
       print("I'd love to go to " + city.title() + "!")