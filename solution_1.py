# solution to problem one on the problem set
# John Dunne 2019-02-17
# This program asks the user to input any positive integer and it will calculate the sum of all numbers between one and that number
# Adapted from the video that we covered in week 4 lectures on Moodle
i = int(input("Please Enter a Positive Integer:")) #Here I am asking the user to enter any positive integer in order to run the program

total = 0       # I am assigning total with a starting value of zero

while i > 0:            # the loop below will continue to execute while the statement i is greater than zero remains true
    total = total + i   # i is added to total and this then becomes the new value of total
    i = i - 1           # the value of i eventually reaches zero and the loop is complete as the while statement above is no longer true

print(total)  # When the while loop has finished the final value will be printed to the screen with this command
