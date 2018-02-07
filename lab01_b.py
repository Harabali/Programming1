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
ex1List = ['red', 'white', 'black', 'red', 'green', 'black']
print(uniqueSortedWords(ex1List))

print(first_n(input('Give a word:'),int(input('Give n:'))))

sum = 0
for i in range(0,5):
    n = int(input('Give {}. number: '.format(i)))
    sum+=n
print('The sum: ',sum)

# main()

# if __name__ == "__main__":
#     main()