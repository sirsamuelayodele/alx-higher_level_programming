#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# Getting the last digit of the number
end_val = abs(number) % 10

# Printing the result as instructed
print("The string Last digit of,")
print(f"the number is {number},")
print(f"the string is {last_digit},", end=" ")

# Checking the conditions for the last digit
if end_val > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print(f"and is less than 6 and not 0")

# Printing a new line
print()
