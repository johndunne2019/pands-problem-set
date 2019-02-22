# Solution to problem 2 on the problem set
# John Dunne 2019-02-19
# This program outputs whether or not today is a day beginning with the letter T

import datetime  # I used the datetime function here in order to allow me to run the if and else statements below

if datetime.datetime.today().weekday() == 1 or datetime.datetime.today().weekday() == 3: # From my research I learned weekdays are defined by numbers with 1 equal to Tuesday and 3 equal to Thursday
    print("Yes- today begins with a T")      # if today is either Tuesday or Thursday this statement will be printed to the screen
else:                                       # The else statement will be executed in the event that the if statement above is not true (not Tuesday or Thursday)
    print("No - Today does not begin with a T")  # If today is not Tuesday or Thursday I have asked for this statement to be printed
# I read about the datetime function here: https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date-in-python
# I researched how to use an "or" statement here which allowed me to check for both Tuesday and Thursday in one line: https://www.w3schools.com/python/python_conditions.asp