#!/usr/bin/python3
# Project name: 2-print_alphabet.py
# Author: sirsamuelayodele of ASA
"""Print the alphabet in lowercase, not followed by a new line."""
for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")
