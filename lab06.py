import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img

def Sigmoid(x):
    y = 1/(1+np.power(np.e,-x))
    return y

def sigmoidGradient(x):
    return Sigmoid(x)*(1-Sigmoid(x))

def histogramOfImg(m):
    h = np.zeros(256)
    for i in range(0,256):
        h[i] = np.sum(m==i)
    return h

def RGB2gray(img):
    gray = np.uint8(0.2989*img[:,:,0] + 0.5870*img[:,:,1] + 0.1140*img[:,:,2])
    return gray

def eraseRows(m):
    mV = np.mean(m)
    meanRows = m.mean(axis=1)
    for i in range(0,m.shape[0]):
        if meanRows[i]>mV:
            m[i,:] = np.zeros(m.shape[1])

def meanFilter(img,ws):
    resImg = np.zeros(img.shape)
    for k in range(0,img.shape[2]):
        for i in range(ws,img.shape[0]-ws):
            for j in range(ws,img.shape[1]-ws):
                resImg[i,j,k] = np.mean(img[i-ws:i+ws,j-ws:j+ws,k])

    return resImg.astype('uint8')

# #EX1:
# x = np.arange(-5,5.01,0.01)
# y = Sigmoid(x)
# gy = sigmoidGradient(x)
#
# plt.plot(x,y,'g-',label='sigmoid')
# plt.plot(x,gy,'y--',label='derivates of sigmoid')
# plt.title('SIGMOID function')
# plt.xlabel('X values')
# plt.ylabel('Y values')
# plt.legend()
# plt.show()

# EX2:
# m = img.imread('flowers.jpg')
# # plt.subplot(3,1,1)
# # plt.imshow(m[:,:,0],cmap='gray')
# # plt.subplot(3,1,2)
# # plt.imshow(m[:,:,1],cmap='gray')
# plt.subplot(2,1,1)
# plt.imshow(m[:,:,1],cmap='gray')
# h = histogramOfImg(m[:,:,1])
# # print(h)
# plt.subplot(2,1,2)
# plt.bar(range(0,256),h)
# plt.show()
#
# #EX3:
# img = img.imread('flowers.jpg')
# # print(img)
# grayImg = RGB2gray(img)
# plt.subplot(2,1,1)
# plt.imshow(grayImg, cmap='gray')
# plt.subplot(2,1,2)
# plt.hist(np.reshape(grayImg,(img.shape[0]*img.shape[1],)),256)
# plt.show()

#EX4:
# img = img.imread('flowers.jpg')
# grayImg = RGB2gray(img)
# eraseRows(grayImg)
# plt.imshow(grayImg,cmap='gray')
# plt.show()

#EX5:
img = img.imread('flowers.jpg')
# grayImg = RGB2gray(img)
filteredImg = meanFilter(img,13)
print(filteredImg.dtype)
plt.imshow(img)
plt.show()
plt.imshow(filteredImg)
plt.show()

