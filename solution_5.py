# This program asks the user to input a positive integer and tells the user whether or not the number is a prime
# John Dunne 2019-02-25
# A prime number is a whole number greater than one thats only factors are one and itself
# Any number that has factor other than one and itself is not a prime number

print("This program takes a positive integer (whole number) and tells you whether it is a prime number") # I added this line to tell the user how the program works
x = int(input("Please Enter a Positive Integer:"))  #The user is asked to input a positive integer. The program will then identify if the number is a prime number or not. 
if x <= 0:    # If the integer entered by the user is less than one the below prompt will print to the screen and ask them to enter only a number greater than one
    print("Prime numbers are greater than one, please enter a positive integer greater than one")
for i in range (2, x):  # A range has been defined between 2 up to but not including the number entered by the user(x).
    if x % i == 0:      # the if statement here will loop through all the numbers starting at 2 up to but not including the number that has been inputted by the user (x) and if any of the numbers are evenly divisible into the number inputted it is not a prime number 
        print (x, "is not a Prime Number")  # the statement here will be printed to the screen if a factor of the integer entered by the user has been found in the range 
        break  # the break statement here will break out of the loop once a factor of the number x has been found, we dont need to continue looping  as once we have found one divisor we have proved the number entered by the user is not a prime number
    else:    # if the if statement above has executed and has not found any factor for the number then this else statement will be executed and the below line will be printed to the screen
        print(x, "is a prime number")   #The number is prime if it has no other factors apart from 1 and itself

# This code is adapted from the example we covered in the week 4 lecture on break and continue keywords - https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops