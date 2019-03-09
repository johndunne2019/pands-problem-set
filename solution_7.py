# This program takes a positive floating point number as input and outputs an approximation of its square root
# John Dunne 2019-03-08

print("This program will calculate an approximate square root of any positive floating point number")
# I have printed this line to the screen in order to give the user some background on what operation will be carried out by this program

import math  #the import math module will be used to calculate the square root of the number entered by the user

x =float(input("Please enter a positive floating point number:"))
# I have asked the user to enter a positive floating point number and this be assigned the value x for the rest of the program

x = math.sqrt(x) # The new value of x will be changed to the square root of x calculated by the math.sqrt module here

print(round(x, 1)) # The result of the math.sqrt calculation above will be rounded to one decimal place when its printed to the screen

# When I first wrote this program the full value of the square root was printed to the screen and so I researched how to use the round function to round to one decimal place
# I read about the math.sqrt module here: https://docs.python.org/3/library/math.html
# I read about the round function here: https://www.programiz.com/python-programming/methods/built-in/round