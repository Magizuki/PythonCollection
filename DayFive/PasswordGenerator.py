#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
pass1 = ''
for n in range(0, nr_letters):
    idx= random.randint(0, len(letters) - 1)
    pass1 += letters[idx]

for n in range(0, nr_symbols):
    idx= random.randint(0, len(symbols) - 1)
    pass1 += symbols[idx]

for n in range(0, nr_numbers):
    idx= random.randint(0, len(numbers) - 1)
    pass1 += numbers[idx]

print(pass1)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
pass2 = ''
slot_letters = nr_letters
slot_symbols = nr_symbols
slot_numbers = nr_numbers

while(slot_letters !=0 or slot_symbols != 0 or slot_numbers != 0):
    pick = random.randint(0, 2)
    if(pick == 0 and slot_letters > 0):
        idx= random.randint(0, len(letters) - 1)
        pass2 += letters[idx]
        slot_letters -= 1
    elif(pick == 1 and slot_symbols > 0):
        idx= random.randint(0, len(symbols) - 1)
        pass2 += symbols[idx]
        slot_symbols -= 1
    elif(pick == 2 and slot_numbers > 0):
        idx= random.randint(0, len(numbers) - 1)
        pass2 += numbers[idx]
        slot_numbers -= 1

print(pass2)

#Other Solution
#Eazy Level
# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

#Hard Level
password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")