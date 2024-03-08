# Imagine you are creating a game that features multiple characters
# You can use a dictionary to store multiple, distinct pieces of data
# this is what is meant by key-value pairs, as shown below 

# As you can see in the terminal: 
# the dictionary stores each key-value as seperate data points
# the first bit is the "key, and the second is the "value"

mobster_0 = {"build": "athletic", "points": "7"}
print(mobster_0["build"])
print(mobster_0["points"])

# Once a dictionary has been defined, new values can be added to it as below 

mobster_0["weapon"] = "tommygun"
print(mobster_0)

# This means you can start with an empty dictionary, and add to it from there. 
# This is helpful for user inputted data

mobster_1 = {} 
mobster_1["build"] = "built"
mobster_1["points"] = "10"
mobster_1["weapon"] = "fists"

print(mobster_1)

# YOu can also modify the values in a dictionary after they have been input
# Say you were coding a game, and mobster_1 picks up a weapon in the middle of combat 
# You would want to switch weapon from fists to machete 

print("Don Julio is currently attacking you with his " + mobster_1['weapon'] + ".")

# But wait! 

mobster_1["weapon"] = "machete"
mobster_1["points"] = 17
print("Don Julio has found a " + mobster_1["weapon"] + "!")

# Additionally (or should I say... subractively) you can remove items from a dictionary after the fact. 

del mobster_1['weapon']
print("You have knocked Julios weapon from his hand") 
print(mobster_1)