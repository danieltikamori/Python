# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_tosplit = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_ammount = bill * tip_as_percent
total_bill = bill + total_tip_ammount
bill_per_person = total_bill / people_tosplit
# final_rounded_pay = round(bill_per_person, 2) / if the second decimal is 0, the function doesn't show it.
final_rounded_pay = "{:.2f}".format(bill_per_person)
message = f"Each person should pay: ${final_rounded_pay}"
print(message)
