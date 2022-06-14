# Draw scatter plot in 3d when data is in python list

from matplotlib import pyplot as plt
x=[1,2,3,4,5]
y=[2,4,5,1,2]
z=[6,7,2,1,9]

#change axes
axes=plt.axes(projection='3d')

axes.scatter(x,y,z)
plt.show()
