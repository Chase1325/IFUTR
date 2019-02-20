#Generate the error and standard deviation heat maps
import matplotlib as m
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse



def heat(samples):

    plt.figure(1) #Z=10
    plt.title('Error Map @ Z=100mm')
    plt.grid(True)
    plt.figure(2) #Z=1225
    plt.title('Error Map @ Z=1225mm')
    plt.grid(True)
    plt.figure(3) #Z=2025
    plt.title('Error Map @ Z=2025mm')
    plt.grid(True)

    plt.figure(4) #Z=10
    plt.title('Standard Deviation Map @ Z=100mm')
    plt.grid(True)
    plt.figure(5) #Z=1225
    plt.title('Standard Deviation Map @ Z=1225mm')
    plt.grid(True)
    plt.figure(6) #Z=2025
    plt.title('Standard Deviation Map @ Z=2025mm')
    plt.grid(True)

    locations = [[]]
    errorData = []
    stdData = []
    #Populate data lists from samples
    for s in samples:
        s.getTrue()
        s.getMean()
        s.getVar()
        s.getStd()
        s.getErr()



    fig1=plt.figure(1)
    fig2=plt.figure(2)
    fig3=plt.figure(3)
    fig4=plt.figure(4)
    fig5=plt.figure(5)
    fig6=plt.figure(6)


    return fig1, fig2, fig3, fig4, fig5, fig6
