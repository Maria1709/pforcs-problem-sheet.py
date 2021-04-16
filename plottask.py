# Author Maria carroll
# Week 8
# https://realpython.com/python-matplotlib-guide/
# Lecture 8 Plotting
# Lecturer: Andrew Beatty

import matplotlib.pyplot as plt # import matplotib to plot our graph
import numpy as np # import numpy to mathematically manipulate the data

def plotFunc():
   
    xpoints = np.array(range(0, 4))
    fpoints = xpoints # = x
    gpoints = xpoints**2 # = x2
    hpoints = xpoints*xpoints*xpoints # = x3

    
    plt.plot(fpoints, 'r', label="f(x)=x") # colour red
    plt.plot(gpoints, 'g', label="g(x)=x²") # colour green
    plt.plot(hpoints, 'y', label="h(x)=x³") # colour yellow

  
    plt.xlabel('X-Axis') # x axis label
    plt.ylabel('Y-Axis') # y axis label

    plt.legend() #shows legend data
    plt.show()   # shows finished graph

plotFunc()

