import sys

def slc(l):
    mV = -1
    prod = 1
    for i in l:
        if i>mV:
            mV=i
        prod*=i
    for i in range(mV,prod+1):
        if i%l[0]==0 and i%l[1]==0 and i%l[2]==0:
            return i

#MAIN
l = []
for n in sys.argv[1:]:
    l.append(int(n))

print(l,slc(l))