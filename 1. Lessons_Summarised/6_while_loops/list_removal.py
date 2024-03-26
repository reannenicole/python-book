# you can use the remove function to remove all
# insatces of a specific value from a list

# say you have a shopping list and have decided you no
# longer want an item

shopping_list = ["apple", "orange", "orange", "pear"]
print(shopping_list)

while "orange" in shopping_list:
    shopping_list.remove("orange")

print(shopping_list)