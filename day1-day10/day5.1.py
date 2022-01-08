import random

# generating alphabet list with upper and lower case.
alphabet = []
for i in range(65, 91):
    alphabet.append(chr(i))
for i in range(97, 123):
    alphabet.append(chr(i))
print(alphabet)

# generating numbers list.
numbers = []
for i in range(0, 10):
    numbers.append(str(i))
print(numbers)

# permitted symbols for password on most websites
symbols = ["!", "#", "@", "$", "&", "(", ")", "+", "*", "%"]

password = []

nr_letters = int(input("How many letters you want in your password: "))
nr_numbers = int(input("How many numbners you want in your password: "))
nr_symbols = int(input("How many symbols you want in your password: "))

# adding letters
for i in range(nr_letters):
    password.append(alphabet[random.randint(0, len(alphabet)-1)])

# adding numbers
for i in range(nr_numbers):
    password.insert(random.randint(0, len(password)-1), random.choice(numbers))

# adding symbols
for i in range(nr_symbols):
    password.insert(random.randint(0, len(password)-1), random.choice(symbols))

print(password)
random.shuffle(password)
new_password = "".join(password)

print(f"Your new password: {new_password}")
