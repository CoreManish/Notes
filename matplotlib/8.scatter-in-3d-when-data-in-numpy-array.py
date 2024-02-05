# Draw scatter plot in 3d when data is in numpy array

from matplotlib import pyplot as plt

import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([2,4,5,1,2])
z=np.array([6,7,2,1,9])

#change axes
axes=plt.axes(projection='3d')

axes.scatter(x,y,z)
plt.show()
