def uniqueSortedWords(list):
    list.sort()
    newList = []
    for str in list:
        if str not in newList:
            newList.append(str)
    return newList


ex1List = ['red', 'white', 'black', 'red', 'green', 'black']
print(uniqueSortedWords(ex1List))