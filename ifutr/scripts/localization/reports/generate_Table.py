#Generate the data tables
import matplotlib as m
import matplotlib.pyplot as plt
import numpy as np

def dataTable(samples):

    celltext_100 = []
    celltext_1225 = []
    celltext_2025 = []

    columns = ('X [mm]', 'Y [mm]', r'$\bar{x}$', r'$\bar{y}$',r'$\bar{e_{xy}}$',
               r'$\bar{\sigma_{xy}}$', r'$\bar{\sigma_{xy}^2}$')

    hcell,wcell=0.5, 1
    hpad,wpad= 1, 0

    for s in samples:
        true = s.getTrue()
        mean = s.getMean()
        var = s.getVar()
        std = s.getStd()
        err = s.getErr()

        if((true[2]==10)or(true[2]==100)):
            celltext_100.append([true[0], true[1], round(mean[0],2), round(mean[1],2),
                                 round(np.average([err[0], err[1]]),2), round(np.average([std[0],std[1]]),2),
                                 round(np.average([var[0],var[1]]),2)])

        if(true[2]==1225):
            celltext_1225.append([true[0], true[1], round(mean[0],2), round(mean[1],2),
                                 round(np.average([err[0], err[1]]),2), round(np.average([std[0],std[1]]),2),
                                 round(np.average([var[0],var[1]]),2)])

        if(true[2]==2025):
            celltext_2025.append([true[0], true[1], round(mean[0],2), round(mean[1],2),
                                 round(np.average([err[0], err[1]]),2), round(np.average([std[0],std[1]]),2),
                                 round(np.average([var[0],var[1]]),2)])

    nrows,ncols = len(celltext_100)+1, len(columns)

    plt.figure(13)
    plt.title('Data Table for Z=100mm')
    ax = plt.gca()
    ax.axis('off')
    ax.table(cellText=celltext_100,colLabels=columns,loc='center')

    plt.figure(14)
    plt.title('Data Table for Z=1225mm')
    ax = plt.gca()
    ax.axis('off')
    ax.table(cellText=celltext_1225,colLabels=columns,loc='center')

    plt.figure(15)
    plt.title('Data Table for Z=2025mm')
    ax = plt.gca()
    ax.axis('off')
    ax.table(cellText=celltext_2025,colLabels=columns,loc='center')


    fig1 = plt.figure(13)
    fig2 = plt.figure(14)
    fig3 = plt.figure(15)

    return fig1, fig2, fig3
