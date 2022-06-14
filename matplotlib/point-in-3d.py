# Draw point in 3d

from matplotlib import pyplot as plt

# change default axes of 2d to 3d
axes=plt.axes(projection='3d')

axes.scatter(8,5,7)
plt.show()
