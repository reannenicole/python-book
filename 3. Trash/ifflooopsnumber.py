start = int(input('What value should we start at? '))
end = int(input('What value should we end at? '))
divide = int(input('What number to check divisibility for? '))
number = start
while number <= end:
    if number % divide == 0:
        print(number, 'is divisible by', divide)
    number += 1