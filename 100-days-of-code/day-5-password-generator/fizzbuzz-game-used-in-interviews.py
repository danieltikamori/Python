# FizzBuzz Game - used in the interviews

# Used input(), for loop, range(), if/elif/else and print()

target = int(input("Enter a number between 0 and 1000: \n")) # or simply a number
for number in range(1, target + 1):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)

# Made by: Daniel Tikamori