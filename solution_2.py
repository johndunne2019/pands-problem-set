# Solution to problem 2 on the problem set
# John Dunne 2019-02-19
# This program outputs whether or not today is a day beginning with the letter T

import datetime  # I have imported the datetime function

if datetime.datetime.today().weekday() == 1 or datetime.datetime.today().weekday() == 3: 
# From my research I learned the weekday function defines weekdays by integers from 0 to 6 with 1 equal to Tuesday and 3 equal to Thursday
    print("Yes- today begins with a T")      # if today is either Tuesday or Thursday this statement will be printed to the screen
else:       # The else statement will be executed in the event that the if statement above is not true (not Tuesday or Thursday)
    print("No - Today does not begin with a T")  # If today is not Tuesday or Thursday I have asked for this statement to be printed

# I imported the datetime module and within the datetime module used the weekday() function which identifies weekdays as integers
# I used an if statement to check if today is the integer equivalent of Tuesday or Thursday and the "or" logical statement to check both conditions in the same line
# I used an else statement to print an output is today is any of the other 5 weekdays
# I read about the datetime function here: https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date-in-python
# I read about the weekday() function here: https://pythontic.com/datetime/date/weekday
# I researched how to use an "or" logical operater here which allowed me to check for both Tuesday and Thursday in one line: https://www.w3schools.com/python/python_conditions.asp