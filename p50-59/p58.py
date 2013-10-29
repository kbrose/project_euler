from array import *

#n = 10000000 # finds primes up to n

#sieve = [1]*n

#sieve[0] = 0
#sieve[1] = 0 # apparently 1 is not prime

#for i in xrange(2, int(n ** 0.5) + 1):
#    for j in xrange(i << 1, n, i):
#        sieve[j] = 0

#def IsPrime(n):
#    return sieve[n]

def IsPrime(n):
    for i in xrange(2, int(n**.5)+2):
        if not n % i:
            return 0
    return 1

n = 25
inc = 4
diags = 9
primes = 5
counter = 0
while 10 * primes > diags:
    inc += 2
    n += inc
    #print n
    if IsPrime(n):
        primes += 1
    n += inc
    #print n
    if IsPrime(n):
        primes += 1
    n += inc
    #print n
    if IsPrime(n):
        primes += 1
    diags += 4
    #counter = counter + 1
    n += inc
    #print n
    #if counter == 2:
    #    quit()


print inc+1
    
