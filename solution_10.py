# This program displays a plot of the functions x, x2 and 2x in the range [0, 4]
# John Dunne 2019-03-24
# I am starting to develop this solution while watching the week 9 lecture videos and further reading on the pyplot tutorial
# Additional reading matplotlib pyplot tutorial: https://matplotlib.org/users/pyplot_tutorial.html 
# From the tutorial I see how to plot an axis
import numpy as np
import matplotlib.pyplot as pl # mathplotlib.pyplot is imported and given a shorter name
plot = pl.plot([0,1,2,3,4], [0,1,2,3,4])  # both the x and y axis have been set to to the range [0,4]
pl.setp(plot, color='r', linewidth= 1.0)
pl.show() # this is the command used to show the plot created above
# I have to plot the functions of x, x2 and 2x