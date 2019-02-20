#Generate the data scatter, std plots, and error bars
import matplotlib as m
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse




def dataMap(samples):

    print(len(samples))
    plt.figure(1) #Z=10
    plt.title('Samples @ Z=100mm')
    plt.grid(True)
    plt.figure(2) #Z=1225
    plt.title('Samples @ Z=1225mm')
    plt.grid(True)
    plt.figure(3) #Z=2025
    plt.title('Samples @ Z=2025mm')
    plt.grid(True)

    iter1 = 0
    iter2 = 0
    iter3 = 0
    colors = ['r',          'b',                'y',        'm',        'g',                    'c',
              'maroon',     'navy',             'olive',    'violet',   'lime',                 'aqua',
              'tomato',     'royalblue',        'orange',   'hotpink',  'mediumspringgreen',    'deepskyblue',
              'orangered',  'mediumslateblue',  'gold',     'crimson',  'darkseagreen',         'teal',
              'chocolate']


    for s in samples:
        data = s.getData()
        mean = s.getMean()
        true = s.getTrue()
        var = s.getVar()
        std = s.getStd()
        err = s.getErr()

        if((true[2]==10)or(true[2]==100)):
            plt.figure(1)

            for i in range(len(data[0])):
                #plt.plot(data[0][i],data[1][i], color=colors[iter1], marker='o', alpha=0.15)
                pass
            #Std Circle
            ax = plt.gca()
            e = Ellipse(xy=(mean[0],mean[1]), width=std[0], height=std[1], color=colors[iter1], alpha=0.5)
            ax.add_patch(e)
            plt.axes(ax)
            plt.plot()

            iter1+=1

        if(true[2]==1225):
            plt.figure(2)
            for i in range(len(data[0])):
                plt.plot(data[0][i],data[1][i], color=colors[iter2], marker='o', alpha=0.15)


            #Std Circle
            ax = plt.gca()
            e = Ellipse(xy=(mean[0],mean[1]), width=std[0], height=std[1], color=colors[iter2], alpha=0.5)
            ax.add_patch(e)
            plt.axes(ax)

            iter2+=1

        if(true[2]==2025):
            plt.figure(3)
            for i in range(len(data[0])):
                plt.plot(data[0][i],data[1][i], color=colors[iter3], marker='o', alpha=0.15)

            #Std Circle
            ax = plt.gca()
            e = Ellipse(xy=(mean[0],mean[1]), width=std[0], height=std[1], color=colors[iter3], alpha=0.5)
            ax.add_patch(e)
            plt.axes(ax)

            iter3+=1

    fig1=plt.figure(1)
    fig2=plt.figure(2)
    fig3=plt.figure(3)

    return fig1, fig2, fig3
