import numpy as np
import GPy
#from IPython.display import display
import matplotlib as m
import matplotlib.pyplot as plt
from scipy import interpolate

#GPy.plotting.change_plotting_library('plotly')

# sample inputs and outputs
x1_data = np.array([1500, 1500, 1500,   2500, 2500, 2500,   500,    500, 500])
x2_data = np.array([1500, 2500, 500,    1500, 2500, 500,    1500,   2500, 500])
y_data = np.array([150,   335,  205,    158,  155,  135,    170,    135, 170])

cmap = m.cm.jet
norm = m.colors.Normalize(vmin=0, vmax=250)

func = interpolate.Rbf(x1_data, x2_data, y_data, function='linear')

xnew, ynew = np.mgrid[0:3000:1, 0:3000:1]

fnew = func(xnew,ynew)

#plt.figure(1) #Z=10
fig, ax = plt.subplots()
plt.title('Error Map @ Z=100mm')
#plt.colorbar(cmap=cmap)
map = ax.pcolormesh(xnew,ynew,fnew, cmap=cmap, norm=norm)
plt.colorbar(map, cmap=cmap, norm=norm)

plt.show()
