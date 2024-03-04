# an if statement takes the results of a conditional test and then
# executes a function based on the result 
# for example: 
# This takes user input, combined with a series of if statements that
# make multiple checks, and the output will differ based on what data it recieves

current_year = int(input('what year is it? '))
received_year = int(input('What year did you get your passport? '))
if received_year + 10 < current_year:
    print('You should go get a new passport!')
if received_year + 10 == current_year:
    print('You should get a new passport sometime soon')
if received_year + 10 > current_year:
    print('You do not need to get a new passport for now')

#in an if statement, indentation plays the same role as it does in a for loop
# meaning that it will stop when the correct conditions have been met
    
