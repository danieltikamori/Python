#1. Create a greeting for your program.
user_name = input("Hello! Welcome to the Band Name Generator! What's your name?\n")
#2. Ask the user for the city that they grew up in.
city_name = input("Ok, " + user_name + "! Now tell me the city you grew up in:\n")
#3. Ask the user for the name of a pet.
pet_name = input("Also tell me the name of your pet:\n")
#4. Combine the name of their city and pet and show them their band name.
band_name = city_name + " " + pet_name
#5. Make sure the input cursor shows on a new line:
print("The name of your band is:\n" + band_name)
print("It have " + str(len(band_name)) + " characters including spaces. Or " + str(len((band_name).replace(" ", ""))) + " without spaces.")