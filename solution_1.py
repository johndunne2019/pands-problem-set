# solution to problem one on the problem set
# John Dunne 2019-02-17
# This program asks the user to input any positive integer and it will calculate the sum of all numbers between one and that number

print("This program takes a positive integer and outputs the sum of all numbers between one and that number")
# I have added this line to explain to the user how this program works

i = int(input("Please Enter a Positive Integer:")) #Here I am asking the user to enter any positive integer in order to run the program
# The positive integer entered by the user will be assigned the variable value of i
if i < 0: # I have added this feature to give the user a message if they enter any number less than zero
    print("Please enter only a positive integer, this program does not operate on negative numbers")
if i > 0: # When a positive integer greater than zero is entered the program runs as below
  i  = i + 1  # I have added one to the value of i as I want to establish a range between 1 and i in the next step
  x = range (1, i) # I have established a range of numbers between 1 and i, i being the number the user entered plus 1 
  print(sum(x)) # I use the sum function to print the sum of all numbers in the range to the screen

# I formulated this solution myself. I have used an if statement to ensure the program is only run where the input is greater than one. 
# I asked for one to be added to the value of the users input and then established a range between 1 and the new value of the variable.
# The reason I increased the value the user entered by one is because this is necessary to have an accurate range.
# The sum function is then used to sum all the numbers in the range and print them to the screen. 
# In this solution I added a feature to return a message to the user asking them to only enter a positive integer if the number entered by them is less than zero.
# Below are details of additional reading and resources I used in developing this solution
# I read about the sum function here: https://www.w3schools.com/python/ref_func_sum.asp and https://docs.python.org/3/library/functions.html
# if statements: https://docs.python.org/3/tutorial/controlflow.html#if-statements and https://www.w3schools.com/python/python_conditions.asp
# Range: https://docs.python.org/3/tutorial/controlflow.html#the-range-function and https://www.w3schools.com/python/ref_func_range.asp