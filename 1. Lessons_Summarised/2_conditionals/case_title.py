# an if test lets your code respond to certain conditions within it
# it does this by checking through a list and, if certain conditions are met, modifies the output
# such as below:

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
   if car == "bmw":
    print(car.upper())
   else:
    print(car.title())