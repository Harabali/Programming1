import random
# import keyboard

# # EX1:
# s1 = set([4,6,8,2,'apple',54,'abcd',2,4,6])
# s2 = {1,6,8,5,68,4,8,2,1,'sg','eq'}
#
# s2.add('newE')
# s2.remove(68)
# s2.update({4,6,8,2,'apple',54,'abcd',2,4,6})
#
#
# for i in s1 | s2:
#     print(i)
#
# print(s2.issuperset(s1))

# # EX2:
# wheel = set(range(1, 37))
#
# even = set(range(2,37,2))
# odd = set(range(1,37,2))   #wheel-even
# reds = {1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36}
# blacks = wheel-reds
# higher = set(range(19,37))
# lower = wheel-higher
#
# # wheel.add('00')
# # wheel.add(0)
# wheel.update({'00',0})
#
# num = random.choice(list(wheel))
#
# sets = {'even':even, 'odd':odd, 'reds':reds, 'blacks':blacks, 'high':higher, 'low':lower}
#
# for s in sets:
#     if num in sets[s]:
#         print('The number {} is {}'.format(num,s))


# EX3:
import time
st = time.time()
primes = set(range(2,5001))
for n in range(2,5001):
    p = n
    while p<=5000:
        p += n
        primes.discard(p)
print(primes)

print(time.time()-st)