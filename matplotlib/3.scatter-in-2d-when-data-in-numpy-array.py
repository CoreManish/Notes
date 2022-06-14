# Draw scatter plot when x and y is in numpy array

from matplotlib import pyplot as plt

import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([2,4,5,1,2])

plt.scatter(x,y)
plt.show()
