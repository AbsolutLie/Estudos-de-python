"""Playful!
This is a simple Python program with an educational purpose for the person who is learning python.
"""

import cmath

print("Choose a number between 1 and 100")
number = int(input())
if number < 1 or number > 100:
    print("Invalid number. Please choose a number between 1 and 10.")
else: 
    if number == 2:
        print("you won!")
    else: 
        print("you lost! The correct number was 2.")