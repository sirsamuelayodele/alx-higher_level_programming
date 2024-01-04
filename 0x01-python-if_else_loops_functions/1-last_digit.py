#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# Getting the last digit of the number
end_val = abs(number) % 10

# Checking the conditions for the last digit
if number < 0:
    end_val = -end_val
print("Last digit of {} is {} and is ".format(number, end_val), end="")
if end_val > 5:
    print("greater than 5")
elif end_val == 0:
    print("0")
else:
    print("less than 6 and not 0")
