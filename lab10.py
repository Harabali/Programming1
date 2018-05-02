import math
import datetime

area = lambda r:r**2*math.pi
l = [2,5,6,8,9]

print(list(map(area,l)))


isSix = lambda n: True if n%6==0 else False
print(list(filter(isSix,l)))

# revName = lambda gn,sn : sn[::-1] + ' ' + gn[::-1]
# gn = input('Your given name:')
# sn = input('Your surname:')
#
# print(revName(gn,sn))


sixN = lambda n : n+10*n+n+100*n+10*n+n

print(list(map(sixN,[1,2,3,4,5,6,7,8])))


days = lambda y1,m1,d1,y2,m2,d2 : str((datetime.date(y2,m2,d2)-datetime.date(y1,m1,d1)).days) + ' days'

print(days(1986,5,23,2018,5,2))