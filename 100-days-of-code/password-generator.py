#Password Generator Project

# Used int(), input(), random.choice(), append(), for loop, shuffle(), join() and print()

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the TikaPassword Generator!")
nr_letters= int(input("How many letters would you like in your password? (Recommended: at least 10)\n"))
nr_symbols = int(input(f"How many symbols would you like? (at least 2)\n"))
nr_numbers = int(input(f"How many numbers would you like? (at least 2)\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# ezpassword = ""

# for char in range(1, nr_letters + 1):
#   ezpassword += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   ezpassword += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   ezpassword += random.choice(numbers)

# print(f"Your password is: {ezpassword}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

# Now we must "convert" the list in a String.
# To do this, we use the join() method or for loop.
# join() method takes all items in an iterable and joins them into one string. A string must be specified as the separator, in this case: ''.
# Note: When using a dictionary as an iterable, the returned values are the KEYS, not the values.

print(f"This is the password before the shuffle: {''.join(password_list)}")

# shuffle() as the name implies, shuffles the list
random.shuffle(password_list)
print(f"This is the password after the shuffle: {''.join(password_list)}")

# another way to take list values and put in one String using for loop:
# To avoid repetition, will generate an alternative password.
alt_password_list = []
for char in range(1, nr_letters + 1):
  alt_password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  alt_password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  alt_password_list += random.choice(numbers)
  
random.shuffle(alt_password_list)

password = ""
for char in alt_password_list:
  password += char
print(f"This is the alternative password using the For loop: {password}")

# Made by: Daniel Tikamori