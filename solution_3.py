# Solution to Problem 3 on the Problem Set
# John Dunne 2019-02-22
# This Program prints all the numbers between 1,000 and 10,000 that are divisible by 6 but not by 12 

print("This Program prints all numbers between 1,000 and 10,000 that are divisible by 6 but not by 12:")
# I have explained to the user what this program does 

for i in range (1000, 10001):        # I have defined the range as being between the numbers 1,000 and 10,000
    if (i % 6 == 0) and (i % 12 != 0):  # The if statement here checks if the numbers between 1,000 and 10,000 are divisible by 6 but not by 12
# the if statement is using the modulo function which checks the remainder when the first argument is divided by the second argument 
        print(i)   # If both conditions of the if statement above are met for numbers between 1,000 and 10,000 the numbers will be printed to the screen

# I developed this program myself drawing on the information from lectures and I researched online to see if the code was efficient or could be improved
# I read about using "and" to combine logical statements here and I used this to ask for both conditions in one line: https://www.w3schools.com/python/python_conditions.asp