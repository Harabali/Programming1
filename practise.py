def sumOfFactors(n):
    sum = 0;
    for i in range(1,int(n/2)+1):
        if n%i==0:
            sum+=i
    return sum


# #--------------------------------------------------
# n = int(input('Give a number:'))
# sumOfFacts = sumOfFactors(n)
# if sumOfFacts == n:
#     print(n, 'is a prefect number')
# elif sumOfFacts < n:
#     print(n,'is a deficient number')
# else:
#     print(n,'is a abundant number')
