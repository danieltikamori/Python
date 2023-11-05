# Used range() function to generate a list of even numbers, for loop, accumulator and print.
target = int(input("Enter a number between 0 and 1000: \n"))

#accumulator
even_sum = 0

# for loop using range(start, stop(excludes the stop value, if want to include the stop value, sum + 1), step)
for even_num in range(2, target + 1, 2):
  even_sum += even_num

print(f"The sum of all even numbers between 0 and {target} is {even_sum}).")