text = input('Type some text and then press ENTER: ')
uppercase_count = 0
lowercase_count = 0

for index in range(0, len(text)):
    char = text[index]
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1

print("Number of upper-case letters:", uppercase_count)
print("Number of lower-case letters:", lowercase_count)

