# This program asks the user to input a positive integer and tells the user whether or not the number is a prime
# John Dunne 2019-02-25
# A prime number is a whole number greater than one thats only factors are one and itself
# Any number that has factor other than one and itself is not a prime number

x = int(input("Please Enter a Positive Integer:"))  #The user is asked to input a positive integer. The program will then identify if the number is a prime number or not. 

for i in range (2, x):  # A range has been defined between 2 and the number entered by the user and this will be used to check for divisors in the if statement below
    if x % i == 0:      # the if statement here will loop through all the numbers between 2 and the number that has been inputted by the user (x) and if any of the numbers are evenly divisible into the number inputted it is not a prime number 
        print ("That is not a Prime Number")  # the statement here will be printed to the screen if the above if statement finds a number in the range that divides the number the user inputted in which case the number is not a prime number 
        break  # the break statement here will break out of the loop once a the if statement above has been proved through, we dont need to continue looping  as once we have found one divisor we have proved the number entered by the user is not a prime number 