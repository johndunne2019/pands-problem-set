# This program reads in a text file from a prompt on the command line and outputs every second line of the text file
# John Dunne 2019-03-14
# This program is adapted from the reading I completed here: https://stackoverflow.com/questions/30551945/how-do-i-get-python-to-read-only-every-other-line-from-a-file-that-contains-a-po
# Returned to add sys.argv after viewing the week 9 lecture on command line arguments
# The sys.argv part of this solution was adapted from the example we covered in lecture on command line arguments: https://web.microsoftstream.com/video/65df155a-ac29-460b-869d-2de6ffc6c3fc

import sys # sys is imported
print(f"This script is called: {sys.argv[0]}") # this original name of the file will be printed
for arg in sys.argv: # for each argument entered on the command line the argument is printed to the screen
    print(arg)
if len(sys.argv) == 2: # if there are 2 arguments entered on the command line this message is printed
   print("The Program is ready to run")
else:   # if more or less than 2 arguments are entered on the command line this line is printed
   print("You can only supply a single filename")
with open ('myfile.txt', 'r') as f:  # with open is used to open the file and I have asked for read mode 
   count = 0  # count is set to 0 for the first iteration of the for loop
   for line in f:  # for loop is used to loop through the lines in the file
      count = count + 1   # 1 is added to the value of count each time the file loops through a line 
      if count % 2 == 0:  # Modulo operator used to establish if the line is an even numbered line (every second line)
         print(line)  # Every second line will be printed as output

# Count is used to assign a starting value of zero to the first line in a file and a for loop will loop through each line of the file
# Every time the loop runs one is added to the value of count and an if statement with modulo operator will identify even numbered lines 
# Example - In the first iteration of the for loop the first line is assigned value of one and thus wont be printed and so on
# Finally all even numbered lines are printed to the screen as output
# We covered this material in the week 7 lecture video- "opening files for reading and writing"
# The with open command is the recommended way to open a file from the command line as the file is closed automatically after operation
# I read about the with open keyword here: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# I have asked for the file to be opened in "r" mode which is read only mode 

# The first steps I completed in solving this problem was to create a file to be read and have some text printed to the file
# Below are the commands I used when setting up the file to be read by this program - myfile.txt
# First command to write to the text file:
#with open('myfile.txt', 'w') as f: 
   # f.write("This file will be used to run the program in solution 9 on the problem set\n")
# Second command to append text to the text file:
#with open('myfile.txt', 'a') as f: 
    #f.write("I have written the text in this file from solution_9.py file\n")
    #f.write("I first asked for the file to open in 'w' mode to write the first line\n")
    #f.write("Opening a file with 'w' overwrites the contents of the entire file\n")
    #f.write("I then used 'a' to append the text here to the existing text\n")
    #f.write("backslash n is used to go to a new line each time\n")
    #f.write("In this program I will attempt to have every second line of the file printed to the screen\n")
    #f.write("In the last line I am not putting a blackslash end")