# Control flow with if / else and Conditional (logical) operators

## if and else statements

```python
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120: # In Python we use : instead of the classic {}. Most languages uses {} to create a if/else statements blocks
  print("You can ride the rollercoaster!")  # Indentation is really important in Python, must be indented to separate the blocks of code.
else: # if and else must be in the same "level" of indentation.
  print("Sorry, you have to grow taller before you can ride.")
```

## Comparison Operators
```python
> - greater than
< - less than
>= - greater than or equal to
<= - less than or equal to
== - equal to. = means assignment
!= - not equal to / different
```

## Modulo (gives the remainder after a division)

The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.

14 % 4 = 2 . Because 4 ÷ 4 = 3 x 4 + 2, remainder is 2.

#### Example:

Odd or even?

```python
number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
```

## Nested statements and elif (else if) statements

```python
if condition1:
  do A
elif condition2:
  do B
elif condition3:
  do C
else:
  do D
```

Example 1 - Rollercoaster ride price:

```python
if height >= 120:
  print("YOu can ride the rollercoaster!")
  age = int(input("What is your age?"))
  if age < 12:    # This if is inside the first if block
    print("Please pay $5.")
  elif age <= 18:
    print("Please pay $7.")
  elif age <65:
    print("Please pay $10.")
  else:
    print("Please pay $12.")
else:
  print("Sorry, you have to grow taller before you can ride.")
```

Example 2 - BMI calculator:

```python

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")
```

Example 3 - Leap year:

```python
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    print("Not leap year.")
elif year % 100 > 0:
    print ("Leap year.")
elif year % 400 == 0:
    print("Leap year.")
else:
    print("Not leap year.")
```

Example 4 - Pizza deliveries

```python
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size =="S":
        bill += 2
    else:
        bill += 3
        
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
```
