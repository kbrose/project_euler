from array import *

primes = array('l',[3])
primes.append(5)

for i in xrange(7,1000000,2):
    PrimeBool = 1
    for prime in primes:
        #if prime == 1:
        #    continue
        if (i % prime)==0:
            PrimeBool = 0
            break
    if PrimeBool:
        primes.append(i)
        print i


def isprime(n):
    return n in primes

def iscirc(n):
    log = 1
    while(n >= log):
        log = log*10
    log = log/10
    rot = (n / 10) + (n % 10)*log
    while not n == rot:
        if not isprime(rot):
            return 0
        rot = (rot / 10) + (rot % 10)*log
    return 1

counter = 13
for i in xrange(100,1000000):
    if isprime(i):
        if iscirc(i):
            counter = counter + 1
            print i, counter

print counter
