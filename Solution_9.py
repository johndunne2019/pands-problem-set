# This program reads in a text file from a prompt on the command line and outputs every second line of the text file
# John Dunne 2019-03-08
with open('myfile.txt', 'w') as f: 
    f.write("This file will be used to run the program in solution 9 on the problem set")
     # I have to save a txt file to be read and return to finish this program to read every second line later

# We covered this material in the week 7 lecture video- "opening files for reading and writing"
# The with open command is the recommended way to open a file from the command line as the file is closed automatically after operation
# I read about the with open keyword here: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# I have asked for the file to be opened in "r" mode which is read only mode 