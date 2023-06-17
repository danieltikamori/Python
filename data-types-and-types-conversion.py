#Data Types

#String

print("Hello"[4]) #Prints the 5th character (count begins at 0)
print("123" + "456")

#Integer

print(123 + 456)

# _ is the same of , in large numbers like 123,456,789.
# 123_45678 = 12345678

#Float
#Floating point number

# Numbers with decimals

pi = 3.14159
pi_times_hundred = 314.159

#Boolean

True
False

# Checking data type using function type()

type("variable or whatever")

type("username")
print(type(pi))

# Converting data type to another (type casting)

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