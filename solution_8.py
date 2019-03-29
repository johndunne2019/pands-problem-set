# This program outputs todays date in the format Monday, January 10th 2019 at 1:15pm
# John Dunne 2019-03-12
# Revisited to add the suffix after the date

import datetime as dt   # I have imported the datetime module and given it the shortened name dt
today= dt. datetime.today()  # today() is used to return the local date and time and it is set equal to the variable today
# I need to have a variable to assign a suffix to the date as requested in the problem
daynumber= int(today.strftime("%d"))  # I introduce the variable daynumber here and set equal to the integer equivalent of the day of the month
# I had to add int to have the integer value %d be recognized and work properly in the below if, elif, else statements
# First I had just - daynumber= today.strftime(%d) and this didnt work correctly
if daynumber == (1, 21, 31): 
    daynumber = 'st'  # if statement used to assign the value 'st' to the 1st, 21st and 31st day of the month
elif daynumber == (29):
    daynumber = 'nd'
else:
    daynumber = 'th' # else statement used to assign the value 'th' to all other days of the month

print(f"The current date and time is: {today.strftime('%A, %B %d')}{daynumber} {today.strftime('%Y at %H:%M%p')}")
# I have used f strings to have all info I needed printed together in the same sentence
# I have asked for today to be printed using strftime which is used to return a string representation of the time
# I introduced a variable called daynumber which will be used to assign a value for the suffix to the date 


# This program uses the datetime module and the strftime function within the datetime module to output the current date and time
# I constructed this program myself using the material we covered in the week 6 lecture as a starting point 
# strftime is used return a string representation of date and time which we studied in the week 6 lectures "modules"
# I completed additional reading on strftime: https://docs.python.org/3/library/datetime.html and https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
# I read about format tokens to format the date output in strftime here: https://stackabuse.com/how-to-format-dates-in-python/ and http://strftime.org/
# I used these format tokens to print the current date and time to the screen in the format requested in the problem