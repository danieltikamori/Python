# Check if a year is leap year or not
year = int(input("Which year do you want to check? Type here: "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 400:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print ("Leap year.")
else:
  print ("Not leap year.")