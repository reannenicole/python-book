# This lesson summarises lists and list manipulation, and goes over the commands .title, .upper, .lower
#.append, .insert, del


# This prints the full list with original syntax

juan_deag = ["reanne", "bland", "rowan", "jim"]
print(juan_deag)

# This prints one of the list, in the written order, starting from 0

print(juan_deag[0])

# This does the same, and capitalises the first letter of the word, making it a "title"

print(juan_deag[0].title())

# There are other functions that will change the capitalisation, such as the below:
# This is helpful for standardising submitte data that may be formatted incorrectly

print(juan_deag[0].upper())
print(juan_deag[0].lower())

# You can also use a negative number in a list when working with a data set you don't know the size of

print(juan_deag[-1])

# using the .append command, you can add to a list after the fact as below:
# this makes it easy to build a list dynamically. You can create define an empty list for future use!

juan_deag.append("finney")
print(juan_deag)

# You can also retroacively change the positioning in a list by using the following: 

juan_deag.insert(0, "pete")
print(juan_deag)

# You can also use the del command to remove an item from a list (if you know its position)

del juan_deag[0]
print(juan_deag)

# You can do a similar thing by using the pop method, which removes it from the list BUT
# allows you to use that item afterwards
# Lets do this with a new list!

my_hobbies = ["dnd", "reading", "movies"]
print(my_hobbies)

popped_my_hobbies = my_hobbies.pop()
print(my_hobbies)
print(popped_my_hobbies)

# But whats the use case? lets say these are types from order of favourite to least favourite
# We could do this: 

least_favourite = my_hobbies.pop()
print(f"my least favourite hobby is {least_favourite.title()}.")

# You can do this from any position is a list!

terry_pratchett = ["Sourcery", "Guards, Guards", "Eric"]

best_pratchett = terry_pratchett.pop(1)
print(f"The greatest Terry Pratchett book is {best_pratchett.title()}.")

# So that's how we can manipulate data by indes, but we can also do it by value!
# You can see now that ones been popped, and ones been removed, the list is only one item!

print(terry_pratchett)
terry_pratchett.remove("Sourcery")
print(terry_pratchett)

# You can even give reasons behind your removals! Lets say we wanted to buy a new console
# And we wanted to filter down the list until we got to the one we wanted

print("============================")
print("==CONSOLE===LIST===CHOICES==")
print("============================")
print("====Which should I buy?=====")

consoles = ["Playstation", "Xbox", "Switch", "NES", "Amigo"]
print(consoles)

too_old = "NES"
consoles.remove(too_old)
print(f"\nA {too_old.title()} is too old to play new games!\n")
print(consoles)


too_expensive = "Playstation"
consoles.remove(too_expensive)
print(f"\nA {too_expensive} is out of my budget!\n")
print(consoles)

doesnt_exist = "Amigo"
consoles.remove(doesnt_exist)
print(f"\nAn {doesnt_exist} is not real!\n")
print(consoles)

handheld = "Switch"
consoles.remove(handheld)
print(f"\nA {handheld} is a handheld, and I want a home console!\n")
print(consoles)
print("\nThat means I should get an Xbox!\n")

# You can find out the length of your list by using the len() command!

teas = ["green", "black", "matcha"]
print(len(teas))