
def greatestDivisor(n):
    d = n-1
    while n%d!=0:
        d-=1
    return d

#MAIN
n = int(input('Give a number:'))
while n!=0:
    div = greatestDivisor(n)
    print(n,div)
    n = int(input('Give a number:'))