# Solution to problem 2 on the problem set
# John Dunne 2019-02-19
# This program outputs whether or not today is a day beginning with the letter T

import datetime

if datetime.datetime.today().weekday() == 1: # 1 is equal to Tuesday and here if it Tuesday I have asked for the below statement to be printed
    print("Yes- today begins with a T")
elif datetime.datetime.today().weekday() == 3: # 3 is for Thursday and if today is Thursday I have used an elif statement to check if today is Thursday
    print("Yes- today begins with a T")
else:                                       # If today is not Tuesday or Thursday I have asked for the below statement to be printed
    print("No - Today does not begin with a T")
# I used the example that we covered in lectures called Tuesday.py which asked is Today Tuesday and I added in an elif statement for Thursday