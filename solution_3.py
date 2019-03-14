# Solution to Problem 3 on the Problem Set
# John Dunne 2019-02-22
# This Program prints all the numbers between 1,000 and 10,000 that are divisible by 6 but not by 12 

print("This Program prints all numbers between 1,000 and 10,000 that are divisible by 6 but not by 12:")
# I have explained to the user what this program does 

for int in range (1000, 10001):    # I have defined the range as being between the numbers 1,000 and 10,000
    if int % 6 == 0 and int % 12 != 0:  # The if statement here checks if the numbers between 1,000 and 10,000 are divisible by 6 but not by 12
# the if statement is using the modulo function which checks the remainder when the first argument is divided by the second argument 
        print(int)   # If both conditions of the if statement above are met for numbers between 1,000 and 10,000 the numbers will be printed to the screen

# I developed this program myself drawing on the information from lectures and additional reading
# I researched the Modulo operator to check remainder after division: https://docs.python.org/3.3/reference/expressions.html
# I read about range here: Range: https://docs.python.org/3/tutorial/controlflow.html#the-range-function and https://www.w3schools.com/python/ref_func_range.asp
# I read about using "and" to combine logical statements here and I used this to ask for both conditions in one line: https://www.w3schools.com/python/python_conditions.asp