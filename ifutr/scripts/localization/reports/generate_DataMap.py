#Generate the data scatter, std plots, and error bars
import matplotlib as m
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse


def dataMap(samples, spacing):

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

    plt.figure(4) #Z=10
    plt.title(r'$\sigma, 2\sigma, 3\sigma$' + ' & errorbar @ Z=100mm')
    plt.grid(True)
    plt.figure(5) #Z=1225
    plt.title(r'$\sigma, 2\sigma, 3\sigma$' + ' & errorbar @ Z=1225mm')
    plt.grid(True)
    plt.figure(6) #Z=2025
    plt.title(r'$\sigma, 2\sigma, 3\sigma$' + ' & errorbar @ Z=2025mm')
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
                plt.plot(data[0][i],data[1][i], color=colors[iter1], marker='o', alpha=0.15)
                pass
            plt.xlim(0, spacing)
            plt.ylim(0, spacing)

            plt.figure(4)
            #Std Circle
            ax = plt.gca()
            sig6 = Ellipse(xy=(mean[0],mean[1]), width=6*std[0], height=6*std[1], color=colors[iter1], alpha=0.25)
            sig4 = Ellipse(xy=(mean[0],mean[1]), width=4*std[0], height=4*std[1], color=colors[iter1], alpha=0.5)
            sig2 = Ellipse(xy=(mean[0],mean[1]), width=2*std[0], height=2*std[1], color=colors[iter1], alpha=0.75)

            ax.add_patch(sig6)
            ax.add_patch(sig4)
            ax.add_patch(sig2)
            ax.arrow(true[0],true[1],mean[0]-true[0],mean[1]-true[1], color='black')
            plt.axes(ax)
            plt.plot()
            plt.plot(mean[0],mean[1],color=colors[iter1], marker='o')
            plt.plot(true[0],true[1],color='black', marker='o')
            plt.xlim(0, spacing)
            plt.ylim(0, spacing)

            iter1+=1

        if(true[2]==1225):
            plt.figure(2)
            for i in range(len(data[0])):
                plt.plot(data[0][i],data[1][i], color=colors[iter2], marker='o', alpha=0.15)
            plt.xlim(0, spacing)
            plt.ylim(0, spacing)


            plt.figure(5)
            #Std Circle
            ax = plt.gca()
            sig6 = Ellipse(xy=(mean[0],mean[1]), width=6*std[0], height=6*std[1], color=colors[iter2], alpha=0.25)
            sig4 = Ellipse(xy=(mean[0],mean[1]), width=4*std[0], height=4*std[1], color=colors[iter2], alpha=0.5)
            sig2 = Ellipse(xy=(mean[0],mean[1]), width=2*std[0], height=2*std[1], color=colors[iter2], alpha=0.75)

            ax.add_patch(sig6)
            ax.add_patch(sig4)
            ax.add_patch(sig2)
            ax.arrow(true[0],true[1],mean[0]-true[0],mean[1]-true[1], color='black')
            plt.axes(ax)
            plt.plot()
            plt.plot(mean[0],mean[1],color=colors[iter2], marker='o')
            plt.plot(true[0],true[1],color='black', marker='o')
            plt.xlim(0, spacing)
            plt.ylim(0, spacing)

            iter2+=1

        if(true[2]==2025):
            plt.figure(3)
            for i in range(len(data[0])):
                plt.plot(data[0][i],data[1][i], color=colors[iter3], marker='o', alpha=0.15)
            plt.xlim(0, spacing)
            plt.ylim(0, spacing)

            plt.figure(6)
            #Std Circle
            ax = plt.gca()
            sig6 = Ellipse(xy=(mean[0],mean[1]), width=6*std[0], height=6*std[1], color=colors[iter3], alpha=0.25)
            sig4 = Ellipse(xy=(mean[0],mean[1]), width=4*std[0], height=4*std[1], color=colors[iter3], alpha=0.5)
            sig2 = Ellipse(xy=(mean[0],mean[1]), width=2*std[0], height=2*std[1], color=colors[iter3], alpha=0.75)

            ax.add_patch(sig6)
            ax.add_patch(sig4)
            ax.add_patch(sig2)
            ax.arrow(true[0],true[1],mean[0]-true[0],mean[1]-true[1], color='black')
            plt.axes(ax)
            plt.plot()
            plt.plot(mean[0],mean[1],color=colors[iter3], marker='o')
            plt.plot(true[0],true[1],color='black', marker='o')
            plt.xlim(0, spacing)
            plt.ylim(0, spacing)

            iter3+=1

    fig1=plt.figure(1)
    fig2=plt.figure(2)
    fig3=plt.figure(3)
    fig4=plt.figure(4)
    fig5=plt.figure(5)
    fig6=plt.figure(6)


    return fig1, fig2, fig3, fig4, fig5, fig6
