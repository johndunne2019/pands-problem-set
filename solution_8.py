# This program outputs todays date in the format Monday, January 10th 2019 at 1:15pm
# John Dunne 2019-03-12

# I have to return to this solution later in order to have the date printed in the format January 10th
print("The current date and time is:") 
import datetime as dt   # I have imported the datetime module which will be used to check the current date and time
today= dt. datetime.today()  # today() is used to return the local date and time and it is set equal to the variable today
print(today.strftime("%A, %B %d %Y at %H:%M%p"))  # I have asked for today to be printed in a specific format

# This program uses the datetime module and the strftime function within the datetime module to output the current date and time
# I constructed this program myseld using the material we covered in the week 6 lecture as a starting point 
# strftime is used return a string representation of date and time which we studied in the week 6 lectures "modules"
# I completed additional reading on strftime: https://docs.python.org/3/library/datetime.html and https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
# I read about format tokens to format the date output in strftime here: https://stackabuse.com/how-to-format-dates-in-python/ and http://strftime.org/
# I used these format tokens to print the current date and time to the screen in the format requested in the problem