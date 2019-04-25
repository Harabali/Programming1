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

properties = {'red':red,'black':black,'even':even,'odd':odd,'small':small,'great':great,'00':set()}

money = int(input('How many dollars in game: '))

while True:
    try:
        bet = int(input('Give your bet: '))
        if bet > money:
            raise IndexError
        pred = input('Next properti of number: ')
        while bet != 0:
            num = random.choice(list(wheel))
            flag=False
            properties[pred]
            if num=='00':
                print('00 is green')
                if pred == '00':
                    print('You won!')
                    money += bet
                    print('Amount of your money: {}'.format(money))
                else:
                    print('You losed!')
                    money -= bet
                    print('Amount of your money: {}'.format(money))
            else:
                for k in properties:
                    if num in properties[k]:
                        print("{} is {}".format(num,k))
                        if pred == k:
                            flag=True
                if flag == True:
                    print("You won!")
                    money += bet
                    print('Amount of your money: {}'.format(money))
                else:
                    print("You losed!")
                    money -= bet
                    print('Amount of your money: {}'.format(money))

            if money == 0:
                break

            bet = int(input('Give your bet: '))
            if bet > money:
                raise IndexError
            pred = input('Next property of number: ')

        if money == 0:
            print('Losed all your money!')
        else:
            print('You win {} dollars!'.format(money))
        break

    except ValueError:
        print('You should give the bet in number format!')
    except KeyError:
        print('You have to choose from the possible properties!')
    except IndexError:
        print('You have to take lesser or equal bet than you money!')
