#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# Getting the last digit of the number
end_val = abs(number) % 10

# Checking the conditions for the last digit
if end_val > 5:
    print("Last digit of {} is {} and is greater than 5".formwat(number, end_val))
elif end_val == 0:
    print("Last digit of {} is {} and is 0".format(number, end_val))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, end_val))

# Printing a new line
print()
