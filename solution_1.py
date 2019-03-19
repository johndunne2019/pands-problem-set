# solution to problem one on the problem set
# John Dunne 2019-02-17
# This program asks the user to input any positive integer and it will calculate the sum of all numbers between one and that number

print("This program takes a positive integer and outputs the sum of all numbers between one and that number")
# I have added this line to explain to the user how this program works

i = int(input("Please Enter a Positive Integer:")) #The user is asked for an input which will be assigned variable value i

if i < 0: # I have added this feature to give the user a message if they enter any number less than zero
    print(f"You have entered a negative number {i}, Please enter a positive number")
    
if i > 0: # The program only runs on positive numbers 
  y  = i + 1  # I have added one to the value of i as I want to establish a range between 1 and i in the next step
  x = range (1, y) # I have established a range of numbers between 1 and the new variable (1 greater than the user input)
  print(f"The sum of all numbers between 1 and {i} is: {sum(x)}") # I use the sum function to print the sum of all numbers in the range to the screen

# I formulated this solution myself. I have used an if statement to ensure the program is only run where the input is greater than one. 
# I asked for one to be added to the value of the users input and then established a range between 1 and the new variable.
# The reason I increased the value the user entered by one is because this is necessary to have an accurate range.
# The sum function is then used to sum all the numbers in the range and print them to the screen. 
# In this solution I added a feature to return a message to the user asking them to only enter a positive integer if the number entered by them is less than zero.
# Below are details of additional reading and resources I used in developing this solution
# I read about the sum function here: https://www.w3schools.com/python/ref_func_sum.asp and https://docs.python.org/3/library/functions.html
# if statements: https://docs.python.org/3/tutorial/controlflow.html#if-statements and https://www.w3schools.com/python/python_conditions.asp
# Range: https://docs.python.org/3/tutorial/controlflow.html#the-range-function and https://www.w3schools.com/python/ref_func_range.asp
# I returned to this solution after watching the week 7 video on fstrings and changed the output message 