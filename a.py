import random


symbols = ["!", "#", "@", "$", "&", "(", ")", "+", "*", "%"]
new_symbols = []
for i in range(5):
    new_symbols.append(symbols[random.randint(1, 5)])
