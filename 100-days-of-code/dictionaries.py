""" Dictionaries

  A dictionary is a collection of key-value pairs.
  A dictionary is written with curly brackets, and each key-value pair is separated by a comma.

  Example:
  {
    "name": "John",
    "age": 30,
    "city": CITY_1
  }
"""
CITY_1 = "New York"
CITY_2 = "London"

#  Accessing the Value
#  You can access the value of a dictionary by using its key.

#  Example:
person = {
    "name": "John",
    "age": 30,
    "city": CITY_1 
}

print(person["name"]) # Output: John

#  Modifying the Value
#  You can modify the value of a dictionary by using its key.

#  Example:
person = {
  "name": "John",
  "age": 30,
  "city": CITY_1
}

person["age"] = 31
print(person["age"]) # Output: 31

#  Adding a New Key-Value Pair #1
#  You can add a new key-value pair to a dictionary by using the update() method.

#  Example:
person = {
  "name": "John",
  "age": 30,
  "city": CITY_1
}

person.update({"country": "USA"})
print(person) # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'country': 'USA'}

# Another way to add items to a dictionary #2
person = {
  "name": "John",
  "age": 30,
  "city": CITY_1
}

person["country"] = "USA"
print(person) # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'country': 'USA'}

#  Removing a Key-Value Pair
#  You can remove a key-value pair from a dictionary by using the pop() method.

#  Example:
person = {
  "name": "John",
  "age": 30,
  "city": CITY_1
}

person.pop("city")
print(person) # Output: {'name': 'John', 'age': 30}

#  Removing all Key-Value Pairs
#  You can remove all key-value pairs from a dictionary by using the clear() method.

#  Example:
person = {
  "name": "John",
  "age": 30,
  "city": CITY_1
}

person.clear()
print(person) # Output: {}

#  Length of a Dictionary
#  You can get the length of a dictionary by using the len() function.

#  Example:
person = {
  "name": "John",
  "age": 30,
  "city": CITY_1
}

print(len(person)) # Output: 3

#  Looping Through a Dictionary
#  You can loop through a dictionary by using a for loop.

# Example:
person = {
  "name": "John",
  "age": 30,
  "city": CITY_1
}

for key, value in person.items():
    print(key, value) # Output: name John, age 30, city New York

#  Looping Through All Keys
#  You can loop through all keys in a dictionary by using just the dictionary itself(recommended)
# or by using the keys() method (not recommended).

#  Example:
person = {
  "name": "John",
  "age": 30,
  "city": CITY_1
}

for key in person:
    print(key) # Output: name, age, city

#  Looping Through All Values
#  You can loop through all values in a dictionary by using the values() method.

#  Example:
person = {
  "name": "John",
  "age": 30,
  "city": CITY_1
}

for value in person.values():
    print(value) # Output: John, 30, New York

#  Looping Through All Items
#  You can loop through all items in a dictionary by using the items() method.

#  Example:
person = {
  "name": "John",
  "age": 30,
  "city": CITY_1
}

for key, value in person.items():
    print(key, value) # Output: name John, age 30, city New York

#  Checking if a Key Exists
#  You can check if a key exists in a dictionary by using the in operator.

#  Example:
person = {
  "name": "John",
  "age": 30,
  "city": CITY_1
}

if "name" in person:
    print("The key 'name' exists in the dictionary.")
    # Output: The key 'name' exists in the dictionary.

# Grading program

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

# 1: Create an empty dictionary called student_grades.
student_grades = {}

# 2: Covert scores into grades.
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)
