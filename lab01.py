def firstNelemnts(list, h):
    if h<=len(list):
        return list[:h]
    else:
        print("There are not enough elements.")
        return []


def productumOfIntegers(list):
    res = 1
    for i in list:
        if i!=0:
            res*=i
    return res


def startBletterAnimalName(list):
    count = 0
    for str in list:
        if 'B' == str[0]:
            count+=1
    return count

def divisionByX(n,x):
    res = []
    for i in range(1,n+1):
        a = int(input('Next n:'))
        if a%x == 0:
            res.append(a)
    return res

def oldAnimals(list):
    for n in list:
        if n[1] < 2000:
            print(n[0], end=' ')
    print('',end="\n")

def oldestAnimal(str):
    min = 2020
    #name=''
    str = str.split('\n')
    for s in str:
        s2 = s.split(':')
        if min>int(s2[1]):
            name = s2[0]
    return name

#main
lista = [10,3,5,7]
res = firstNelemnts(lista,3)
print(res)


lista2 = [10,0,-2,3,5,0]
print(productumOfIntegers(lista2))

lista3 = ['Lion', 'Monkey', 'Cat', 'Dog', 'Boxi', 'Butterfly']
print(startBletterAnimalName(lista3))

#print(divisionByX(3,5))

allatok = [('Buddy', 1999), ('Andy', 2013), ('Tom', 2000), ('Jerry', 1998)]
oldAnimals(allatok)

adat = """Néró:2015
Buksi:1999
Pamacs:2009"""
print(oldestAnimal(adat))


