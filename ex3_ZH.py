


#MAIN
fin = open('input.txt','r')
fout = open('output.txt','w')

for r in fin:
    nums = r.split(';')
    print(nums)
    maxV = -1000
    for n in nums:
        if int(n)>maxV:
            maxV = int(n)
    print(maxV)

fin.close()
fout.close()