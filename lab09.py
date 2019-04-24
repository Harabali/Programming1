import random
import keyboard

# EX1:
# s1 = set([4,6,8,2,'apple',54,'abcd',2,4,6])
# s2 = {1,6,8,5,68,4,8,2,1,'sg','eq'}
#
# s2.add('newE')
# s2.remove(68)
# s2.update({4,6,8,2,'apple',54,'abcd',2,4,6})
#
#
# for i in s1 ^ s2:
#     print(i)
#
# print(s2.issuperset(s1))

# EX2:
import random
wheel = set(range(0,37))

red = {1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36}
black = wheel-red
even = set(range(0,37,2))
odd = wheel-even
small = set(range(0,19))
great = wheel-small

wheel.add('00')

prop = {'red':red,'black':black,'even':even,'odd':odd,'small':small,'great':great}
bet = input('Give your bet: ')
while True:
    if bet not in prop:
        bet = input('Give your bet again: ')
    else:
        num = random.choice(list(wheel))
        if num=='00':
            print('00 is green')
        else:
            for k in prop:
                if num in prop[k]:
                    print('{} is {}'.format(num,k))
            if num in prop[bet]:
                print('You win!')
                break
            else:
                print('You lose!')
                bet = input('Give your bet again: ')


# EX3:
primes = set(range(2,5001))
for n in range(2,5001):
    p = n
    while p<=5000:
        p += n
        primes.discard(p)
print(primes)
