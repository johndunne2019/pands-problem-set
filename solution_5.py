# This program asks the user to input a positive integer and tells the user whether or not the number is a prime
# John Dunne 2019-02-25
# A prime number is a whole number greater than one thats only factors are one and itself
# Any number that has factor other than one and itself is not a prime number
# Adapted from - https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops

print("This program takes a positive integer (whole number) and tells you whether it is a prime number")
# I added this line to tell the user how the program works
number = int(input("Please Enter a Positive Integer:"))  
#The user is asked to input a positive integer. The program will then identify if the number is a prime number or not. 
if number <= 1:    # If the integer entered by the user is less than or equal to one the below prompt will print to the screen
    print(f"Prime numbers are greater than 1, you have entered: {number} Please enter a number greater than 1")
if number > 1:  # Prime numbers are greater than one and so I have asked for the loop to run only for numbers greater than one
  for i in range (2, number):  # A range has been defined between 2 up to but not including the number entered by the user.
    if number % i == 0:      # the if statement here will run within the for loop through all the numbers starting at 2 up to but not including the number that has been inputted by the user and if any of the numbers are evenly divisible into the number inputted it is not a prime number 
        print (f"{number} That is not a Prime")  # the statement here will be printed to the screen if a factor of the integer entered by the user has been found in the range 
        break  # the break statement here will break out of the loop once a factor of the number x has been found, we dont need to continue looping
  else:    # if no factor was found in the if statement above the else statement here will run
        print(f"{number} That is a prime")   #The number is prime if it has no other factors apart from 1 and itself

# This code is adapted from the example we covered in the week 4 lecture on break and continue keywords - https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
# I have also added a feature whereby if the user enters a number less than or equal to 1 they are prompted to enter only a positive number.
# I read about break here: Break: https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops 
# After viewing the week 7 lecture on fstrings I changed my program to include that feature