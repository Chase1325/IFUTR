#Generate the error and standard deviation heat maps
import matplotlib as m
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse
from scipy import interpolate



def heat(samples, spacing):

    plt.figure(7) #Z=10
    plt.title('Error Map @ Z=100mm')
    plt.grid(True)
    plt.figure(8) #Z=1225
    plt.title('Error Map @ Z=1225mm')
    plt.grid(True)
    plt.figure(9) #Z=2025
    plt.title('Error Map @ Z=2025mm')
    plt.grid(True)

    plt.figure(10) #Z=10
    plt.title('Standard Deviation Map @ Z=100mm')
    plt.grid(True)
    plt.figure(11) #Z=1225
    plt.title('Standard Deviation Map @ Z=1225mm')
    plt.grid(True)
    plt.figure(12) #Z=2025
    plt.title('Standard Deviation Map @ Z=2025mm')
    plt.grid(True)


    #Generate Z=100mm maps first
    locX_100 = []
    locY_100 = []
    errorData_100 = []
    stdData_100 = []

    locX_1225 = []
    locY_1225 = []
    errorData_1225 = []
    stdData_1225 = []

    locX_2025 = []
    locY_2025 = []
    errorData_2025 = []
    stdData_2025 = []

    #Populate data lists from samples
    for s in samples:
        true = s.getTrue()
        mean = s.getMean()
        var = s.getVar()
        std = s.getStd()
        err = s.getErr()

        if((true[2]==10)or(true[2]==100)):
            locX_100.append(true[0])
            locY_100.append(true[1])
            errorData_100.append(np.average([err[0], err[1]]))
            stdData_100.append(np.average([std[0], std[1]]))

        if((true[2]==1225)):
            locX_1225.append(true[0])
            locY_1225.append(true[1])
            errorData_1225.append(np.average([err[0], err[1]]))
            stdData_1225.append(np.average([std[0], std[1]]))

        if((true[2]==2025)):
            locX_2025.append(true[0])
            locY_2025.append(true[1])
            errorData_2025.append(np.average([err[0], err[1]]))
            stdData_2025.append(np.average([std[0], std[1]]))

    #Convert to numpy arrays
    locX_100 = np.asarray(locX_100)
    locY_100 = np.asarray(locY_100)
    errorData_100 = np.asarray(errorData_100)
    stdData_100 = np.asarray(stdData_100)
    print(errorData_100)

    locX_1225 = np.asarray(locX_1225)
    locY_1225 = np.asarray(locY_1225)
    errorData_1225 = np.asarray(errorData_1225)
    stdData_1225 = np.asarray(stdData_1225)

    locX_2025 = np.asarray(locX_2025)
    locY_2025 = np.asarray(locY_2025)
    errorData_2025 = np.asarray(errorData_2025)
    stdData_2025 = np.asarray(stdData_2025)
    #Generate Error Heatmaps

    cmap = m.cm.jet
    norm = m.colors.Normalize(vmin=0, vmax=250)
    xnew, ynew = np.mgrid[0:spacing:10, 0:spacing:10]

        #Z=100 Error heatmap
    plt.figure(7) #Z=10
    func = interpolate.Rbf(locX_100, locY_100, errorData_100, function='linear')
    fnew = func(xnew,ynew)
    ax = plt.gca()
    map = ax.pcolormesh(xnew,ynew,fnew, cmap=cmap, norm=norm)
    plt.colorbar(map, cmap=cmap, norm=norm)
    plt.axes(ax)
    plt.xlim(0, spacing)
    plt.ylim(0, spacing)
    plt.plot()


        #Z=1225 Error heatmap
    plt.figure(8) #Z=10
    func = interpolate.Rbf(locX_1225, locY_1225, errorData_1225, function='linear')
    fnew = func(xnew,ynew)
    ax = plt.gca()
    map = ax.pcolormesh(xnew,ynew,fnew, cmap=cmap, norm=norm)
    plt.colorbar(map, cmap=cmap, norm=norm)
    plt.axes(ax)
    plt.xlim(0, spacing)
    plt.ylim(0, spacing)
    plt.plot()


    #Z=2025 Error heatmap
    plt.figure(9) #Z=10
    func = interpolate.Rbf(locX_2025, locY_2025, errorData_2025, function='linear')
    fnew = func(xnew,ynew)
    ax = plt.gca()
    map = ax.pcolormesh(xnew,ynew,fnew, cmap=cmap, norm=norm)
    plt.colorbar(map, cmap=cmap, norm=norm)
    plt.axes(ax)
    plt.xlim(0, spacing)
    plt.ylim(0, spacing)
    plt.plot()

    #Z=100 STD heatmap
    plt.figure(10) #Z=10
    func = interpolate.Rbf(locX_100, locY_100, stdData_100, function='linear')
    fnew = func(xnew,ynew)
    ax = plt.gca()
    map = ax.pcolormesh(xnew,ynew,fnew, cmap=cmap, norm=norm)
    plt.colorbar(map, cmap=cmap, norm=norm)
    plt.axes(ax)
    plt.xlim(0, spacing)
    plt.ylim(0, spacing)
    plt.plot()


    #Z=1225 STD heatmap
    plt.figure(11) #Z=10
    func = interpolate.Rbf(locX_1225, locY_1225, stdData_1225, function='linear')
    fnew = func(xnew,ynew)
    ax = plt.gca()
    map = ax.pcolormesh(xnew,ynew,fnew, cmap=cmap, norm=norm)
    plt.colorbar(map, cmap=cmap, norm=norm)
    plt.axes(ax)
    plt.xlim(0, spacing)
    plt.ylim(0, spacing)
    plt.plot()

    #Z=2025 STD heatmap
    plt.figure(12) #Z=10
    func = interpolate.Rbf(locX_2025, locY_2025, stdData_2025, function='linear')
    fnew = func(xnew,ynew)
    ax = plt.gca()
    map = ax.pcolormesh(xnew,ynew,fnew, cmap=cmap, norm=norm)
    plt.colorbar(map, cmap=cmap, norm=norm)
    plt.axes(ax)
    plt.xlim(0, spacing)
    plt.ylim(0, spacing)
    plt.plot()

    fig1=plt.figure(7)
    fig2=plt.figure(8)
    fig3=plt.figure(9)
    fig4=plt.figure(10)
    fig5=plt.figure(11)
    fig6=plt.figure(12)


    return fig1, fig2, fig3, fig4, fig5, fig6
