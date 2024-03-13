# by nesting a list into a dictionary, you make make the value of the key into multiple items 
# this is demonstrated below: 

pizza = {
    "crust": "thick", 
    "toppings": ["cheese", "peppers"]
}

print("You have ordered a " + pizza["crust"] + " crust pizza" + " with the following toppings: ")
for topping in pizza["toppings"]:
    print("\t" + topping)

# you can do this anytime you want more than a single value to be assigned to a key
    
favourite_films = {
    "bella": ["dune", "poor things"],
    "edward": ["saltburn", "hackers"],
    "jacob": ["the core", "moonfall"]
}

for name, films in favourite_films.items():
    print("\n" + name.title() + "'s favourite films are:")
    for film in films:
        print("\t" + film.title())

    
