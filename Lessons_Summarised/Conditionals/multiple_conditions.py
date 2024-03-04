# If you need multiple conditions to be true before executing code, and not just one
# we omit the elif and else from the chain

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
 print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
 print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
 print("Adding extra cheese.")

print("\nyour pizza is done!")