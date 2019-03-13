# This program outputs todays date 
# John Dunne 2019-03-12

import datetime as dt   # I have imported the datetime module which will be used to check the current date and time
today= dt. datetime.today()  # I have asked the datetime module to make today equal to the current date and time
print(today.strftime("%A, %B %d %Y at %H:%M%p"))

# We looked at strftime in week 6 lectures on modules: https://docs.python.org/3/library/datetime.html 
# I read about format tokens to format the date output in strftime here: https://stackabuse.com/how-to-format-dates-in-python/