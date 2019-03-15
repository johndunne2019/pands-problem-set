# This program reads in a text file from a prompt on the command line and outputs every second line of the text file
# John Dunne 2019-03-14

with open ('myfile.txt', 'r') as f:
   for line in f:
      print(line)
     # I can also use a for loop to print the lines in the file"

# We covered this material in the week 7 lecture video- "opening files for reading and writing"
# The with open command is the recommended way to open a file from the command line as the file is closed automatically after operation
# I read about the with open keyword here: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# I have asked for the file to be opened in "r" mode which is read only mode 

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