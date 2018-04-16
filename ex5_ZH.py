import numpy as np
import matplotlib.pyplot as mpl

def twoDtooneD(m):
    newV = np.zeros(m.size)
    ind = 0
    for i in range(0,m.shape[0]):
        for j in range(0,m.shape[1]):
            newV[ind] = m[i,j]
            ind+=1
    return newV


#MAIN
m = np.random.randint(0,50,(25,40))
v = twoDtooneD(m)
mpl.plot(np.arange(0,v.size),v)
mpl.show()