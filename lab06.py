import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def Sigmoid(x):
    y = 1/(1+np.power(np.e,x))
    return y

def histogramOfImg(m):
    h = np.zeros(255)
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            h[m[i,j]]+=1
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

def meanFilter(img):
    resImg = np.zeros(img.shape)
    for i in range(2,img.shape[0]-2):
        for j in range(2,img.shape[1]-2):
            resImg[i,j] = np.mean(img[i-2:i+2,j-2:j+2])
    return resImg

#EX1:
# x = np.arange(-3,3,0.1)
# y = Sigmoid(x)
#
# plt.plot(x,y,'g-')
# plt.xlabel('X values')
# plt.ylabel('Y values')
# plt.show()

# EX2:
# m = np.random.randint(0,255,(600,800))
# h = histogramOfImg(m)
# plt.bar(np.arange(0,255,1),h)
# # plt.hist(np.reshape(m,600*800),255)
# plt.show()

#EX3:
# img = mpimg.imread('flowers.jpg')
# # print(img)
# grayImg = RGB2gray(img)
# # grayImg = grayImg.astype(np.uint8)
# # print(grayImg.dtype)
# # plt.imshow(grayImg,cmap='gray')
# # plt.hist(np.reshape(grayImg,grayImg.size),255)
# plt.hist(np.reshape(img[:,:,0],grayImg.size),255,fc='r')
# plt.hist(np.reshape(img[:,:,1],grayImg.size),255,fc='g')
# plt.hist(np.reshape(img[:,:,2],grayImg.size),255,fc='b')
# plt.show()

#EX4:
# img = mpimg.imread('flowers.jpg')
# grayImg = RGB2gray(img)
# eraseRows(grayImg)
# plt.imshow(grayImg)
# plt.show()

#EX5:
# img = mpimg.imread('flowers.jpg')
# grayImg = RGB2gray(img)
# filteredImg = meanFilter(grayImg)
# plt.imshow(grayImg)
# plt.show()
# plt.imshow(filteredImg)
# plt.show()

