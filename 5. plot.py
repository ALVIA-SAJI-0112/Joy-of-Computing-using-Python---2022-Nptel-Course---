#to plot different nos
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
"""
in python, it automatically generates x values for the graph if we don't pass any'
"""

plt.plot([1,2,3,4],[1,4,9,16])
#to label x and y axis
plt.ylabel("some values")
plt.xlabel("some other values")

#to plot in dots
plt.plot([1,2,3,4],[1,4,9,16],'ro')

#to plot in red dashes
plt.plot([1,2,3,4],[1,4,9,16],'r--')

#to plot in blue squares
plt.plot([1,2,3,4],[1,4,9,16],'bs')

#to plot in green triangles
plt.plot([1,2,3,4],[1,4,9,16],'g^')