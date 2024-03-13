multiples_three = list(range(3,1000,3))
multiples_five = list(range(5, 1000, 5))

print(sum(set(multiples_three + multiples_five)))