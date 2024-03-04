name = input("What is your name? ")
age = int(input("How old are you? "))
location = input("Where are you from? ")

print("So, just so I have this correct your name is " + name)
print("You are " + str(age) + " years old")
print("you are from " + location)

current_year = 2024 

print ("and you were born in " + str(current_year - age))

if age > 18:
    print("That means you're old enough to drink!")
else: 
    print("You're too young to drink")
