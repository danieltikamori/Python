# Python Data Types

## String

```python
print("Hello"[4]) #Prints the 5th character (count begins at 0)
print("123" + "456")
```

## Integer

```python
print(123 + 456)

# _ is the same of , in large numbers like 123,456,789.
# 123_45678 = 12345678
```

## Float

### Floating point number

Numbers with decimals

```python
pi = 3.14159
pi_times_hundred = 314.159
```

## Boolean

True
False

## Checking data type using function type()

```python
type("variable or whatever")

type("username")
print(type(pi))
```

## Converting data type to another (type casting)

```python
# To string - str()
new_string_pi = str(pi)

# To integer - int()
new_int_pi = int(pi)

# To float - float()
new_float_pi = float(pi)

# Round float numbers - round(variable, int)
rounded_pi = round(pi, 2) # Round to 2 decimals

# There's really various ways to round number with Python. See documentation.
# Important to note that if the last decimal is 0, it is "omitted", use the function below to show the 0:
rounded_pi = "{:.2f}".format(pi)
```

Example code using strings + variable:

```python
# f"Text with {variable} and more text after."

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
