import random

def rollDices(number_of_dices):
    return sum([random.randint(1, 6) for i in range(number_of_dices)])

print(sum([rollDices(1) for i in range(100000)])/100000)
    