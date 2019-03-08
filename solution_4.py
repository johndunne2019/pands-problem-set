# This is my solution to solution 4 on the problem set
# John Dunne 2019-02-27
# This program asks the user to input any positive integer and then performs a calculation known as Collatz Conjecture
# The calculation takes the current value and if it is even the value is divided by 2 and if it is odd multiplied by 3 and add 1 
# With Collatz Conjecture no matter what the starting value is the sequence will always reach 1 
# This program ends when the current value is 1

print("This program takes a positive integer and performs the Collatz Conjecture calculation and terminates when the current value is 1")

x = int(input("Please Enter a Positive Integer:"))   # The user is asked to input a positive integer which will be the starting point of the calculation

print(x)      # I want the integer the user has inputted to be printed to the screen and the new values after the calculations below will follow

while x > 1:  # I want the the below statements to run only when the value of x is greater than 1 as I want the program to finish when the value reaches 1
    if x % 2 == 0: # this if statement checks the remainder when x is divided by 2 determing if the number is even or odd
        x = x //2   # if the current value of x is even then the new value of x is set to the current value divided by 2 
    else:  # if the above if statement proved false and the current value of x is odd then the below calculation is run instead
        x = 3 * x + 1  # if the current value of x is odd then the new value of x is set to the current value multiplied by 3 plus 1 
    print(x)   # The loop above will run and calculate the new value of x as long as the while statement remains true (x greater than 1)

    # In the end I have asked for the values of x that have been calculated throughout the loop to be printed to the screen. 
    # The program ends when x is equal to 1 as the while loop has asked only for the conditions within to run while x is greater than 1 