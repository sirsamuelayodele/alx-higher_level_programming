#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev = 0
    integer = 0
    for i in roman_string:
        if num[i] > prev:
            integer += num[i] - prev - prev
            prev = num[i]
        else:
            integer += num[i]
            prev = num[i]
    return integer
