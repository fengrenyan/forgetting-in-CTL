import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

Z = np.loadtxt('totalAveTime.txt').reshape((10,10))
X=[5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
#X1=[10, 15, 20, 25, 30, 35, 40, 45, 50]

print(Z)
#Y = np.arange(-5, 5, 0.25)
Y = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

fig = plt.figure(figsize=(15,15), dpi=100)

#ax = fig.gca(projection='3d')
ax = fig.add_subplot(111, projection='3d')
#ax.view_init(40,300
j=0
'''
for i in Y:
    Zz=Z[j]
    j = j+1
    Zx=Zz.reshape((1,10))
    print(Zx)
    ax.plot_surface(X, Y, Zx, cmap='rainbow', antialiased=False, shade=False, linewidth=0, vmin=0.25, vmax=0.35)
'''
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, antialiased=False, vmin=-1000, vmax=2000)
#surf = ax.plot_surface(X, Y, Z, cmap='rainbow', antialiased=False, shade=False, linewidth=0, vmin=0.25, vmax=0.35);

#ax.plot_surface(X, Y, Z, cmap='jet', rstride=1, cstride=1, antialiased=False, shade=False, alpha=1.0, linewidth=0, vmin=0.25, vmax=0.35);
#ax.invert_yaxis()
#ax.dist = 11

#ax = fig.add_subplot(2, 1, 2)
#plt.imshow(Z, cmap='jet', vmin=0.25, vmax=0.35, origin='lower');

plt.savefig('totalAveTime.png')

