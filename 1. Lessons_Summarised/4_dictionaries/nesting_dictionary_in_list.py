# you can store dictionaries in lists, lists in dictionaries, 
# dictionaries in dictionaries, etc. This is called nesting: 

# lets say that you have a cast of characters in a tv show, you want a dictionary for each
# and then you want to group them all together as the cast, heres how youd do it 

character_1 = {"name": "ian", "role": "leading man", "age": "29"}
character_2 = {"name": "jennifer", "role": "leading woman", "age": "28"}
character_3 = {"name": "albert", "role": "comic relief", "age": "35"}

cast = [character_1, character_2, character_3]

for character in cast:
    print(character)

# from here you can add new characters to your list as needed 
    
character_4 = {"name": "samantha", "role": "seductress", "age": "25"}

cast.append(character_4)

for character in cast:
    print(character) 

# you can also add on mass
    
background_characters = {"name": "various", "role": "background actor", "age": "range between 23 - 48"}

for background_characters in range(10):
    background_characters = {"name": "various", "role": "background actor", "age": "range between 23 - 48"}
    cast.append(background_characters)

for character in cast: 
    print(character) 

# theoretically, this could then be amneded after the fact
    
for background_characters in cast[5:9]: 
    if background_characters["name"] == "various":
        background_characters["role"] = "extra"

for character in cast: 
    print(character)
