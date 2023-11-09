# How For loops work

# for loops are used to iterate over a sequence (either a list, a tuple, a dictionary, a set, or a string).

list_of_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for item in list_of_items:
    # do something to each item
    print(item)
for number in range(a, b):
    # do something to each number
    print(number)

# How While loops work

# while loops are used to repeat a block of code as long as a certain condition is true.
x = 0
while x < 10:
    print(x)
    x += 1

something_is_true = True

def do_something():
    """
    This function does something.
    """
    print("something")

while something_is_true:
    # do something repeatedly
    do_something()
    if something_else_is_true:
        break

while not something_is_true:
    # do something repeatedly
    do_something()
    if something_else_is_true:
        break

# Example of break

x = 0
while x < 10:
    print(x)
    x += 1
    if x == 3:
        break

list_of_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for item in list_of_items:
    if item == 3:
        break
    print(item)

# Example of continue

x = 0
while x < 10:
    x += 1
    if x == 3:
        continue
    print(x)

# Example of pass

x = 0
while x < 10:
    x += 1
    if x == 3:
        pass
    print(x)

# Example of else

x = 0
while x < 10:
    print(x)
    x += 1
else:
    print("x is no longer less than 10")

# do while - Python does not have do while loop constructs, must be emulated
# https://realpython.com/python-do-while/
# Use a while Loop and the break Statement
# Use an infinite while loop with a break statement wrapped in an if statement that checks a given condition and breaks the iteration if that condition becomes true:

while True:
    # Do some processing...
    # Update the condition...
    if condition:
        break

>>> while True:
...     number = int(input("Enter a positive number: "))
...     print(number)
...     if not number > 0:
...         break
...
Enter a positive number: 1
1
Enter a positive number: 4
4
Enter a positive number: -1
-1

