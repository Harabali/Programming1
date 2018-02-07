import math

def GCD(n1,n2):
    if n1>n2:
        n1,n2=n2,n1
    div = 1
    for n in range(1,n1+1):
        if n1%n==0 and n2%n == 0:
            div = n
    return div

def dist(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def sumOfDigits(n):
    sum = 0
    while n>0:
        sum+=n%10
        n//=10
    return sum

def uniqueSortedWords(list):
    list.sort()
    newList = []
    for str in list:
        if str not in newList:
            newList.append(str)
    return newList


def first_n(str,n):
    if len(str) <= n:
        return str
    else:
        res = str[:n]
        return res


# def main():


#EX1:
a = int(input('Give a number: '))
while a != 0:
    if a%2 == 0:
        print('{} is even.'.format(a))
    else:
        print('{} is odd.'.format(a))
    a = int(input('Give a number: '))


#Ex2:
str = input('Give two numbers and seperate with colon: ')
a,b = str.split(',')
print(a,b)
print(GCD(int(a),int(b)))

#Ex3:
s1 = input('Give the (x,y) coordinates of the first point: ')
s2 = input('Give the (x,y) coordinates of the second point: ')
x1,y1 = s1.split()
x2,y2 = s2.split()
print('The Euclidean distance between ({},{}) and ({},{}) points is {:.3f}'.format(x1,y1,x2,y2,dist(int(x1),int(y1),int(x2),int(y2))))

#Ex4:
n = int(input('Give a decimal number: '))
print('The sum of digits: {:d}'.format(sumOfDigits(n)))

#Ex5:
ex1List = ['red', 'white', 'black', 'red', 'green', 'black']
print(uniqueSortedWords(ex1List))

#Ex6:
print(first_n(input('Give a word:'),int(input('Give n:'))))


# sum = 0
# for i in range(0,5):
#     n = int(input('Give {}. number: '.format(i)))
#     sum+=n
# print('The sum: ',sum)

# main()

# if __name__ == "__main__":
#     main()