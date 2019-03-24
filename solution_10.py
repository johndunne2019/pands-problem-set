# This program displays a plot of the functions x, x2 and 2x in the range [0, 4]
# John Dunne 2019-03-24
# I am starting to develop this solution while watching the week 9 lecture videos and further reading on the pyplot tutorial
# Additional reading matplotlib pyplot tutorial: https://matplotlib.org/users/pyplot_tutorial.html 
# From the tutorial I see how to plot an axis
import numpy as np
import matplotlib.pyplot as pl # mathplotlib.pyplot is imported and given a shorter name
pl.plot([0,1,2,3,4], color='r', linewidth= 2.0, linestyle= '--')  #plot the range of [0,4]
# I formatted the line that will be plotted using the attributes that I read about in the 'controlling line properties' section of the pyplot tutorial
pl.xlabel("x axis", fontsize=12, fontweight= 'bold') #adding name to x and y axis (read in pyplot tutorial text section)
pl.ylabel("y axis", fontsize=12, fontweight= 'bold') #added a font size and font weight to the x and y axis labels
pl.title("Plot Generated from Solution_10.py", fontsize= 14, fontweight='bold') 
# Adding a title to the plot and formatting as read in the text section of the pyplot tutorial
pl.show() # this is the command used to show the plot created above
# I have to plot the functions of x, x2 and 2x
# I have to return later to plot x2 and 2x