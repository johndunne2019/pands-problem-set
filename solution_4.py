# This is my solution to solution 4 on the problem set
# John Dunne 2019-02-27
# This program asks the user to input any positive integer and then performs a calculation known as Collatz Conjecture
# The calculation takes the current value and if it is even the value is divided by 2 and if it is odd multiplied by 3 and add 1 
# With Collatz Conjecture no matter what the starting value is the sequence will always reach 1 
# This program ends when the current value is 1
print("This program takes a positive integer and performs the Collatz Conjecture calculation and terminates when the current value is 1")
# I have printed a line to the screen to tell the user what operation this program will complete
def odd_even(): # I have created a function inside of which a while loop will be executed when the user passes their input in
  x = int(input("Please Enter a Positive Integer:"))   # The user is asked to input a positive integer which will be the starting point of the calculation
  print(x, end = ' ')  # I want the integer the user has inputted to be printed to the screen first as the starting point of the output
  while x > 1:  # While loop runs when x is greater than 1, otherwise program will be stuck in an infinite loop
    if x % 2 == 0: # I have used the modulo operator to determine if the number is even or odd
        x = x //2   # if the current value of x is even then the new value of x is set to the current value divided by 2 
    else:  # if the current value was odd the if statement above is passed and the else statement here sets the current value of x in next line
        x = 3 * x + 1  # For odd numbers the new value of x is set to the current value multiplied by 3 plus 1 
    print(x, end = ' ')   # I have asked for the output to be printed horizontally on the screen using end = ' ' 

odd_even()  # Here I have called the function to be run, the commands inside the function will run and the output will be printed to the screen
# The program ends when x is equal to 1 as the while loop has asked only for the conditions within to run while x is greater than 1 
# The program will get stuck in an infinite loop if the while loop isnt set to run for numbers greater than 1 only
# We covered functions in week 6 lectures and I also did supplementary reading here: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
# I read about printint integers horizontally here: https://stackoverflow.com/questions/8437964/python-printing-horizontally-rather-than-current-default-printing