import numpy as np
import matplotlib.pyplot as plt

def readData(fin,delimiter):
    datas = []
    for str in fin:
        tmp=str.split(delimiter)
        for i in range(0,len(tmp)):
            tmp[i] = float(tmp[i])
        datas.append(tmp)
    return datas

def plotDatas(X,y,marker):
    plt.plot(X,y,marker)
    plt.xlabel('Population of Cities in 10,000s')
    plt.ylabel('Profit in $10,000s')

def MSE(X,y,theta):
    m = len(y)
    return np.sum((theta.dot(X.T)-y)**2)/(2*m)

def gradient_descent(X, y, theta, alpha, num_iters):
    m = len(y)
    J_history = np.zeros(num_iters)
    for i in range(num_iters):
        h = theta.dot(X.T)
        errors = h - y
        delta = X.T.dot(errors)
        theta -= (alpha / m) * delta
        J_history[i] = MSE(X, y, theta)
        # if i%100==0:
        #     plotDatas(X[:,1],theta.dot(X.T),'g--')
    return (theta, J_history)

fin = open('ex1data1.txt')
ls = readData(fin,',')
data = np.array(ls)
m = len(data)

X = data[:,0]
y = data[:,1]

plotDatas(X,y,'b*')
X = np.stack((np.ones((m,)), X),axis=1)
theta = np.zeros(2)#np.array([-0,1.3])#

# plotDatas(X[:,1],theta.dot(X.T),'r-')
# print(MSE(X,y,theta))
# plt.show()

alpha = 0.01
num_iters = 1500
theta, J_history = gradient_descent(X, y, theta, alpha, num_iters)

# plt.plot(range(0,len(J_history)),np.array(J_history))
# plt.show()

plotDatas(X[:,1],theta.dot(X.T),'r-')
plt.show()