# you can use a while loop to add items to a 
# user inputted dictionary 
# say you are polling a group of people at an event

# start with an empty dictionary 
responses = {}

# set a flag to indicate polling is active 
polling_active = True

while polling_active:
    name = input("\nWhat is your first name? ").title()
    question_1 = input("How did you get here today? ")

    responses[name] = question_1

    repeat = input("Would another person like to answer? (yes/no) ")
    if repeat == "no": 
        polling_active = False

# once polling_active becomes false
# print results
print("\n~~~~ Poll Results ~~~~")
for name, question_1 in responses.items():
    print(f"{name} got here by {question_1}")