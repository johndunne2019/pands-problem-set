# This program takes a positive floating point number as input and outputs an approximation of its square root
# John Dunne 2019-03-08

print("This program will calculate an approximate square root of any positive floating point number")
# I have printed this line to the screen in order to give the user some background on what operation will be carried out by this program
import math  #the import math module will be used to calculate the square root of the number entered by the user
x =float(input("Please enter a positive floating point number:"))
# I have asked the user to enter a positive floating point number which the program will operate on
y = x # I have added a second variable y as I want to have 2 variables printed to the screen in my final output
y = math.sqrt(x) # The new value of y will be changed to the square root of x calculated by the math.sqrt module here
y = (round(y, 1)) # The result of the math.sqrt calculation above will be rounded to one decimal place using the round function
print("The square root of", x, "is approx", y)  # The output is printed to the screen showing the variables x and y
# When I first wrote this program the full value of the square root was printed to the screen and so I researched how to use the round function to round to one decimal place
# I read about the math.sqrt module here: https://docs.python.org/3/library/math.html
# I read about the round function here: https://www.programiz.com/python-programming/methods/built-in/round