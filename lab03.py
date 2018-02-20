import sys
import random

def fillList(args):
    list1 = []
    list2 = []
    flag=0
    for x in args:
        if x == 'L:':
            flag += 1
            continue
        if flag==1:
            list1.append(x)
        if flag==2:
            list2.append(x)
    return list1,list2

def sumOfFirstN(n,outFile):
    sum = 0
    s=''
    for i in range(1,n+1):
        s += str(i) + '+'
        sum += i
    s = s[0:-1] + '=' + str(sum)
    print(s,file=outFile)

def secondsToTime(n,outFile):
    tmp = n
    year = n//(3600*24*365)
    n=n%(3600*24*365)
    day = n//(3600*24)
    n = n%(3600*24)
    hour = n//3600
    n = n%3600
    min = n//60
    sec = n%60
    print('{} seconds is {} year {} day {} hours {} minutes and {} seconds'.format(tmp,year,day,hour,min,sec))

def sumOfChars(string):
    sum = 0
    tmp = ''
    flag = False
    for ch in string:
        if '0' <= ch <= '9':
            tmp+=ch
            flag = True
        else:
            if flag:
                sum += int(tmp)
            tmp = ''
            flag = False
    return sum

# #EX0:
# program_name = sys.argv[0]
# print('The name of my program is', program_name)
# print(len(sys.argv))
# for x in sys.argv[1:]:
#     print(x)

# #EX1:
# list1,list2 = fillList(sys.argv[1:])
# for e in list1:
#     if e in list2:
#         list1.remove(e)
# print(list1)

# #EX2:
# n = int(sys.argv[1])
# outFile = open(sys.argv[2],'w')
# sumOfFirstN(n,outFile)
# outFile.close()

# #EX3:
# n = int(sys.argv[1])
# outFile = open(sys.argv[2],'w')
# secondsToTime(n,outFile)
# outFile.close()

# #EX4:
# print(sumOfChars(sys.argv[1]))

