# This program displays a plot of the functions x, x2 and 2x in the range [0, 4]
# John Dunne 2019-03-24
# I am starting to develop this solution while watching the week 9 lecture videos and further reading on the pyplot tutorial
# Additional reading matplotlib pyplot tutorial: https://matplotlib.org/users/pyplot_tutorial.html 
# From the tutorial I see how to plot an axis
import numpy as np # numpy module is imported and given the short name np
import matplotlib.pyplot as pl # mathplotlib.pyplot module is imported and given a shorter name pl
x = np.arange(start = 0, stop = 4) #The range is defined as being between 0 and 4 using the numpy.arange function
# Using numpy.arange to set the range between 0 and 4 using start and stop parameters
pl.xlabel("x axis", fontsize=12, fontweight= 'bold') #adding name to x and y axis (read in pyplot tutorial text section)
pl.ylabel("y axis", fontsize=12, fontweight= 'bold') #added a font size and font weight to the x and y axis labels
pl.title("Plot Generated from Solution_10.py", fontsize= 14, fontweight='bold') 
# Adding a title to the plot and formatting as read in the text section of the pyplot tutorial

a = x # a is set to the value of x 
b = x*x # b is set to the value of x squared
pl.plot(a, c='r', lw= 4.0, ls= '--') # I have asked for a to be plotted with a red line 
#c short for color, ls short for linestyle and lw short for linewidth
# I formatted the line that will be plotted using the attributes that I read about in the 'controlling line properties' section of the pyplot tutorial
pl.plot(b, c='g', lw= 4.0, ls= '--') # I have asked for b to be ploteed with a green line
pl.show() # this is the command used to show the plot created above