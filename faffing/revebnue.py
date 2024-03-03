Wages = int(input('Wages: '))
Rent = int(input('Rent: '))
Debt = int(input("Debt: "))
Train = int(input("Train: "))
Driving = int(input("Driving: "))
Nictotine = int(input("Nicotine: "))

Leftover = Wages - Rent - Debt - Train - Driving - Nictotine

print('Your amount left after necessary outgoings is ' + str(Leftover))

Savings = int(input("Savings: "))

Living_costs = Leftover - Savings

print("Your amount left after necesseties and savings is " + str(Living_costs))