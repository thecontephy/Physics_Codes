import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

fig = plt.figure()
ax = plt.axes(projection="3d")

a=float(input("Enter the value of lattice constant?")) #2.46 for Graphene
kx = np.arange(-1, 1, 0.025)
ky = np.arange(-1, 1, 0.025)
kx, ky = np.meshgrid(kx, ky)

t=float(input("What is the nearest neighbour hopping energy?")) #2.8 eV for Graphene
z = t*(1+4*(np.cos((3/2)*kx*a))*(np.cos((1.732/2)*ky*a))+4*(np.cos((1.732/2)*ky*a)**2))**(0.5)

Epos = ax.plot_surface(kx, ky, z, color='yellow')

Eneg = ax.plot_surface(kx, ky, -z, color='blue')

ax.set_xlabel('kx')
ax.set_ylabel('ky')
ax.set_zlabel('E(k)')

plt.show()
