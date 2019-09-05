# FE 595: HW 1 - Python Refresher 
# Asna Fatima Ali - 10443256

import matplotlib.pyplot as plt
import numpy as np

# To create the x axis from 0 to 2pi for one period. Step is a small number to create more points and smoother line on the graph
x = np.arange(0,2*np.pi,0.00001)

plt.plot(x,np.sin(x), color = "blue", label = "Sine") # to plot the sine function

plt.plot(x,np.cos(x), color = "orange", label = "Cosine") # to plot cosine function

plt.title("Sine and Cosine Function for One Period", fontsize= 14, fontweight = 'bold')

plt.xlabel("Frequency")

plt.ylabel("Amplitude")

plt.legend(loc='lower left', frameon=False)

plt.show()
