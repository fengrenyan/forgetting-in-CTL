from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt

from matplotlib import cm

from matplotlib.ticker import LinearLocator, FormatStrFormatter

import numpy as np

 

 

fig = plt.figure()

ax = fig.gca(projection='3d')

 

# Make data.

#X = np.arange(-5, 5, 0.25)
X=[5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
#X1=[10, 15, 20, 25, 30, 35, 40, 45, 50]


#Y = np.arange(-5, 5, 0.25)
Y = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
#Y1=[5, 10, 15, 20, 25, 30, 35, 40, 45]


X, Y = np.meshgrid(X, Y)

R = np.sqrt(X**2 + Y**2)

#Z = np.sin(R)
'''
Z=np.loadtxt("proNum.txt").reshape((9,10))




# Plot the surface.

surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,

                       linewidth=0, antialiased=False)

 


	
# Customize the z axis.

#ax.set_zlim(-1.01, 1.01)

#ax.zaxis.set_major_locator(LinearLocator(10))

ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

 

# Add a color bar which maps values to colors.

#fig.colorbar(surf, shrink=0.5, aspect=5)


ax.set_title('Number of formulas')
ax.set_xlabel('Length of 3CNF')
ax.set_ylabel('Number of variables')

plt.savefig('proNum.png')


'''

Z1 = np.loadtxt("numPercent.txt").reshape((10,10))
#surf1 = ax.plot_surface(X, Y, Z1, cmap=cm.coolwarm,

 #                      linewidth=0, antialiased=False, vmin=-1, vmax=1000)
surf = ax.plot_surface(X, Y, Z1, cmap=cm.coolwarm, rstride=1, cstride=1, antialiased=False, shade=False, alpha=1.0, linewidth=0, vmin=0, vmax=79)

print(Z1)
#fig.colorbar(surf1, shrink=0.5, aspect=5)		

elev=15
azim=75
ax.view_init(elev=elev, azim=azim)
#ax.set_title('Time(s)')
#ax.set_title('Number of formulas')
ax.set_zlabel('Propotion(%)')
ax.set_xlabel('Length of 3CNF')
ax.set_ylabel('Number of variables')


plt.savefig('numPercent.png')
#'''
#plt.show()
