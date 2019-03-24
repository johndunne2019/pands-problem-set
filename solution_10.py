# This program displays a plot of the functions x, x2 and 2x in the range [0, 4]
# John Dunne 2019-03-24
# I formulated this solution using the week 9 lectures as a starting point followed by further reading and research which is detailed further in the references section in the Readme file
# Additional reading included the matplotlib pyplot tutorial as recommended in lectures: https://matplotlib.org/users/pyplot_tutorial.html 

print("The Plot should appear on your screen momentarily") # I have returned this line to the user when the script is run
import numpy as np # numpy module is imported and given the short name np
import matplotlib.pyplot as pl # mathplotlib.pyplot module is imported and given a shorter name pl
x = np.arange(start = 0, stop = 4) #The range is defined as being between 0 and 4 using the numpy.arange function
# Using numpy.arange to set the range between 0 and 4 using start and stop parameters
pl.xlabel("x axis", fontsize=12, fontweight= 'bold') # Adding name to x and y axis (read in pyplot tutorial text section)
pl.ylabel("y axis", fontsize=12, fontweight= 'bold') # Added a font size and font weight to the x and y axis labels
pl.title("Plot Generated from Solution_10.py", fontsize= 14, fontweight='bold') 
# Adding a title to the plot and formatting as read in the text section of the pyplot tutorial

a = x # I introduced a variable called a set it equal to the value of x 
b = x*x # I introduced a variable called b and set it equal to the value of x squared
c = 2**x # I introduced a variable called C and set it equal to 2 to the power of x. ** the power operator is used

pl.plot(a, c='r', lw= 4.0, ls= '--', label= 'x') # I have asked for 'a' to be plotted with a red line 
# c short for color, ls short for linestyle and lw short for linewidth
# I formatted the line that will be plotted using the attributes that I read about in the 'controlling line properties' section of the pyplot tutorial
pl.plot(b, c='g', lw= 4.0, ls= '--', label= 'x²') # I have asked for 'b' to be plotted with a green line
pl.plot(c, c='y', lw= 4.0, ls= '--', label= '2x') # I have asked for 'c' to be plotted with a yellow line

pl.legend(loc= 'upper left') # This command shows the legend on the plot, I have given the names in pl.plot above using label
# I have used loc and upper left ask for the legend to be placed in the top left corner of the plot
pl.show() # This is the command used to show the plot created above