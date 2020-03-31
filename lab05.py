import numpy as np

def isSorted(v):
    if v.size == 1:
        return True
    if v[0]<=v[1]:
        for i in range(1,v.size):
            if v[i-1] > v[i]:
                return False
        return True
    else:
        for i in range(1,v.size):
            if v[i-1] < v[i]:
                return False
        return True

def isRowCOlSumsEq(m):
    colSum = m.sum(axis=0)
    rowSum = m.sum(axis=1)
    ref = colSum[0]
    for n in colSum:
        if ref != n:
            return False
    ref = rowSum[0]
    for n in rowSum:
        if ref != n:
            return False
    return colSum.sum() == rowSum.sum()

def indicesOfSpecialCols(m):
    listOfInd=[]
    for i in range(0,m.shape[1]):
        if np.sum(m[:,i]==0) > 0:
            if np.sum(m[:,i]==0)*2 <= np.sum(m[:,i]<0):
                listOfInd.append(i)
    return listOfInd

def listOfSpecialElements(m):
    listOfElemnets = []
    for i in range(0,m.shape[0]):
        for j in range(0,m.shape[1]):
            if m[i,j]%(i+1) == 0 and m[i,j]%(j+1) == 0:
                listOfElemnets.append((m[i,j],i+1,j+1))
    return listOfElemnets

def sortMatrixbyColumn(m,ind):
    for i in range(0,m.shape[0]):
        for j in range(i+1,m.shape[0]):
            if m[i,ind] > m[j,ind]:
                # m[i,:],m[j,:] = m[j,:],m[i,:]
                tmp = m[i,:].copy()
                m[i,:] = m[j,:].copy()
                m[j,:] = tmp.copy()

# EX1:
v = np.random.randint(10,45,15)
v.sort()
print(isSorted(v[::-1]))

# # EX2:
# m = np.random.randint(10,45,(4,5))
# print(m)
# ind = int(input('Give me a index of selected column:'))
# sortMatrixbyColumn(m,ind)
# print(m)
# print(m[np.argsort(m[:,ind])])


# # EX3:
# m = np.random.randint(1,2,(5,5))
# print(m)
# print(isRowCOlSumsEq(m))

# # EX4:
# str = input('Give the shape of array:')
# n,m = str.split(',')
# m = np.random.randint(-5,6,(int(n),int(m)))
# print(m)
# print(indicesOfSpecialCols(m))

# EX5:
m = np.random.randint(10,45,(4,5))
print(m)
print(listOfSpecialElements(m))

