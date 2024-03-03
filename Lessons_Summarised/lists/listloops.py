# a for loop will go through a list and pull each bit of data in it seperatley,
# until the list is done.
# Bwlow, the list is defined normally, and using the "for" function assigns each enrty to a new variable
# called "characters", then prints them. 

dune_characters = ["paul", "chani", "fayd", "gurney", "stilgar"]
for characters in dune_characters:
    print(characters)

# We cn add to this function usings strings or variables!
    
message = "and I can't wait to see the third!"
    
dune_characters = ["Paul", "Chani", "Fayd", "Gurney", "Stilgar"]
for characters in dune_characters:
    print(characters.title() + " was the best character in Dune 2!")
    print(message + ".\n")

# And to break out of the loop, just unindent. As it isn't in the loop, it only prints once!
    
print("Great job everyone")
