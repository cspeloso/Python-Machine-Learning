import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

plotPoints = [[-2,-1], [1,1], [3,2]]

f = np.poly1d([5,1])

x = np.linspace(0,10,30)
y = f(x) + 6*np.random.normal(size=len(x))
xn = np.linspace(0,10,200)

m,c = np.polyfit(x,y,1)
yn = np.polyval([m, c], xn)

plt.plot(x,y,'or')
plt.plot(xn, yn)
plt.show()