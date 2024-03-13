# copying a list means taking the initial one, and being able to ass to it without altering the first!
# we do this by using list slicing, but not quanifying a start or end point!
# this puts the initial list into a new variable, where it can be changed from there!

year_one_classes = ["english", "maths", "science"]
all_classes = (year_one_classes[:])

print("The classes you will take first year are: ")
print(year_one_classes)

all_classes.append("art")
all_classes.append("history")

print("\nThe classes you will take thereafter are: ")
print(all_classes)


