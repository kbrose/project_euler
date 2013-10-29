from array import *

primes = array('l',[0])

for i in xrange(1,100000):
    PrimeBool = 1
    for j in xrange(2, (int)(i**.5)+1):
        if((i % j) == 0):
            PrimeBool = 0
            break
    primes.append(PrimeBool)

def isprime(n):
    if(n < 0):
        return 0
    if(n > 100000):
        PrimeBool = 1
        for j in xrange(2, (int)(i**.5)+1):
            if((n % j) == 0):
                PrimeBool = 0
                break
        return PrimeBool
    return primes[n]

maxlen = 0
maxa = 0
maxb = 0

for a in xrange(-999, 999, 2):
    for b in xrange(0, 999):
        if(isprime(b)):
            counter = 0
            n = 0
            while isprime(n**2 + (a * n) + b):
                n = n + 1
                counter = counter + 1
            if(counter > maxlen):
                maxa = a
                maxb = b
                maxlen = counter

print maxa * maxb
