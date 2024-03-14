# coversley to a break statement, a continue statement
# will loop back round to the beginning based on the conditional 
# for example, lets say you wanted to print number 1-10 
# but only the odd numbers in that range, we can use a continue to do this

# set current number to 0 
current_number = 0

# current number = 0 means it is less than 10, so while statement is true, and we enter the loop 

while current_number < 10:
    # we go up in incriments of one. the modulo is checking for anything divisible by two    
    current_number += 1
    if current_number % 2 == 0:
       # if it is divisible by two, we go back to the start of the loop until it has ran through range
       continue
    print(current_number)