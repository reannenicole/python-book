# Imagine you are creating a game that features multiple characters
# You can use a dictionary to store multiple, distinct pieces of data
# this is what is meant by key-value pairs, as shown below 

# As you can see in the terminal: 
# the dictionary stores each key-value as seperate data points
# the first bit is the "key, and the seconf is the "value"

mobster_0 = {"build": "athletic", "points": "7"}
print(mobster_0["build"])
print(mobster_0["points"])

# you can add new values to a dictionary after the fact, and even create a blank dictionary
# to add stuff to in the future (think user submitted data, list of scores, etc)

mobster_1 = {}
print (mobster_1)

mobster_1["build"] = "chubby"
mobster_1["points"] = "9"

print(mobster_1)
print(mobster_1["build"])

new_points = mobster_1["points"]

print(f"If you kill Pauly, you earn {new_points} points!")

# You can even modify the value of a key after the fact

mobster_1["alive"] = "yes"
print(f"The mobster is currently {mobster_1["alive"]}.")

