from array import *

n = 1000000 # finds primes up to n

sieve = [1]*n

sieve[0] = 0
sieve[1] = 0 # apparently 1 is not prime

for i in xrange(2, int(n ** 0.5) + 1):
    for j in xrange(i << 1, n, i):
        sieve[j] = 0
        
primes = [2]
for i in xrange(3,n):
    if sieve[i]:
        primes.append(i)

currprime = 0
currmax = 0

for start in xrange(0,len(primes)):
    s = primes[start]
    i = start+1
    counter = 1
    tempmax = 1
    for i in xrange(start+1,len(primes)-1):
        s = primes[i] + s
        if s > 999999:
            break
        i = i + 1
        counter = counter + 1
        if sieve[s]:
            tempmax = counter
            tempprime = s
    if tempmax >= currmax:
        currmax = tempmax
        currprime = tempprime
        
print currprime,currmax
