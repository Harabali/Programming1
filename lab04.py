import numpy as np
import time as t

def inverseVector(a):
    b = np.array(a[a.size-1])
    for i in range(a.size-2,-1,-1):
        b = np.append(b,a[i])
    return b


def sortVector(v):
    n = v.size
    for i in range(0,n):
        for j in range(i+1,n):
            if v[i] > v[j]:
                v[i],v[j] = v[j],v[i]
    return v

#EX1:
a = np.arange(10,50)
b = inverseVector(a)
print(a)
print(b)

#EX2:
b = np.array(np.ceil(100*np.random.random((30))),dtype='uint8')
minB = b.min()
maxB = np.max(b)
print(b)
print(minB, maxB)
ind = np.where((b==minB) | (b==maxB))
print(ind)

#EX3:
d = np.random.randint(1,100,15)
d[d==d.max()]=-1
print(d)

#EX5:
c = np.arange(-3,15)
c[(c<8) & (c>3)] = -1
print(c)

#EX6:
d = np.random.randint(1,50,15)
n = int(input('Give a number:'))
e = np.abs(d-n)
print(d)
print(d[e==e.min()])

#EX7:
e = np.random.randint(1,50,15)
print(e)
start = t.time()
e1 = sortVector(e)
ended = t.time()
print(e1)
print('{:.15f}'.format(ended-start))