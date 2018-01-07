import neural
import numpy as np
import matplotlib.pyplot as plt

fig,ax = plt.subplots(1,1)

x = np.arange(-4,4,0.1)
y = np.zeros(x.shape)

i = 0
for X in x:
    y[i] = neural.logistic(X)
    i = i+1
    
ax.plot(x,y)

plt.show()
