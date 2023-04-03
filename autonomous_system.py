import numpy as np
import matplotlib.pyplot as plt

def Ffun(X, Y):
    return (2 - Y) * Y

X, Y = np.meshgrid(np.arange(0, 6.2, 0.2), np.arange(-1, 3.2, 0.2))
DY = Ffun(X, Y)
DX = np.ones_like(DY)

plt.quiver(X, Y, DX, DY, color='black')
plt.contour(X, Y, DY, levels=[0, 1, 2], colors='green')
plt.title('Slope field and isoclines for f(x,y)=(2-y)y')
plt.show()
