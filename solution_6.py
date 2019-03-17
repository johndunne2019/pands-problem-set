# This program takes a user input string and outputs every second word
# John Dunne 2019-03-12
# In order to achieve this I have used the .split function we covered in week 7 lectures 
# I also completed additional resarch and learnt about the * shortcut to unpack lists in python
# I used the * to unpack the list and sep= ' ' to have the separator set as whitespace
# During my testing of the program I can see punctuation such as quotation marks and commas will be printed to the screen as the separator is set to be whitespace

print("This program takes an input string from the user and outputs every second word")
# First I have printed a line to the screen telling the user what the program does
s = str(input("Please enter a sentence:")).split()[::2]
# I have asked the user to input a sentence and then used the .split function to split the complete sentence into every second word
# I have called the split with 2 colons to represent the first and last words entered by the user and a step of 2 to print every second word
# I first wrote the program this way and called the print function straight away but my output was formatted inside square brackets:[Hello, World]
# I then researched how to unpack the list and have used the * shortcut for this
print(*s, sep=' ')
# Here I have asked for the list that was defined in the .split function above to be printed in string format separated by whitespace
# I read how to use the shortcut *s here: https://www.reddit.com/r/learnpython/comments/6b96j3/beginner_how_to_remove_square_bracket_and/
# We covered the .split and .join functions in week 7 lecture fstrings: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str