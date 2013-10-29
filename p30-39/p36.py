from array import *

def ispal(n):
    worker = n
    tester = 0
    while worker > 0:
        tester = tester * 10 + (worker % 10)
        worker = worker / 10
    if not n==tester:
        return 0

    binlen = 0
    worker = n
    binarr = [-1]*25
    while worker > 0:
        binarr[binlen] = worker % 2
        binlen = binlen + 1
        worker = worker / 2
    i = 0
    j = binlen-1
    while binlen > 0:
        if not binarr[i]==binarr[j]:
            return 0
        i = i+1
        j = j-1
        binlen = binlen-2

    return 1

sum = 0
for i in xrange(0,1000000):
    if ispal(i):
        sum = sum + i

print sum


    
