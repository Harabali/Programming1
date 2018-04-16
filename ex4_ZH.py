import numpy as np

def raiseOdds(v):
    for i in range(0,v.size):
        if v[i]%2==1:
            v[i]+=1

#MAIN
v = np.random.randint(0,50,30)
print(v)
raiseOdds(v)
print(v)