import random
import string

# List of all lowercase and uppercase letters
letters = list(string.ascii_lowercase + string.ascii_uppercase)

# List of all digits 0-9
numbers = list(string.digits)

# List of all punctuation symbols
symbols = list(string.punctuation)

# print("Letters:", letters)
# print("Numbers:", numbers)
# print("Symbols:", symbols)

nr_letters = int(input("How many letters do you want? "))
nr_numbers = int(input("How many numbers do you want? "))
nr_symbols = int(input("how many symbols do you want? "))

random.shuffle(letters)
#print(letters)
random.shuffle(numbers)
random.shuffle(symbols)

password = []
for i in range (0, nr_letters):
    password.append(letters[i])
    print(password)
for i in range(0, nr_numbers):
    password.append(numbers[i])
    print(password)
for i in range(0, nr_symbols):
    password.append(symbols[i])
    print(password)
random.shuffle(password)
print(password)

