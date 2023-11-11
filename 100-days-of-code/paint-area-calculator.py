# Calculates the number of cans of paint needed to paint a wall
import math  # to use math.ceil() that rounds up the number


# As it is difficult to buy a fraction of a can, we must round up the number of cans.
def paint_calc(height, width, cover):
  num_cans = (height * width) / cover
  round_up_cans = math.ceil(num_cans)
  print(f"You'll need {round_up_cans} cans of paint. Total area of {heigh_wall * width_wall} m2")

# Define a function called paint_calc() so the code below works.   

height_wall = int(input("Insert the height of the wall in meters: ")) # Height of wall (m)
width_wall = int(input("Insert the width of the wall in meters: ")) # Width of wall (m)
coverage = 5 # Area of a can of paint (m2), modify according to your needs

paint_calc(height=height_wall, width=width_wall, cover=coverage)
