from array import *
from itertools import permutations

n = 10000 # finds primes up to n

sieve = [1]*n

sieve[0] = 0
sieve[1] = 0 # apparently 1 is not prime

for i in xrange(2, int(n ** 0.5) + 1):
    for j in xrange(i << 1, n, i):
        sieve[j] = 0

ps = []
for i in xrange(3,len(sieve),2): # ignores 2, unnecessary to check for this problem
    if sieve[i]:
        ps.append(i)

def IsPrime(n):
    if n < 10000:
        return sieve[n]
    for i in xrange(2,int(n**.5)+1):
        if not (n % i):
            return 0
    return 1

def concat(n, m):
    s1 = str(n)
    s2 = str(m)
    return int(s1 + s2)

length = len(ps)
for i in xrange(0,length-4):
    #print i, len(ps)
    for j in xrange(i+1, length-3):
        if IsPrime(concat(ps[i],ps[j])) and \
                IsPrime(concat(ps[j],ps[i])):
            for k in xrange(j+1, length-2):
                if IsPrime(concat(ps[i],ps[k])) and \
                        IsPrime(concat(ps[k],ps[i])) and \
                        IsPrime(concat(ps[j],ps[k])) and \
                        IsPrime(concat(ps[k],ps[j])):
                    for l in xrange(k+1, length-1):
                        if IsPrime(concat(ps[i],ps[l])) and \
                                IsPrime(concat(ps[l],ps[i])) and \
                                IsPrime(concat(ps[j],ps[l])) and \
                                IsPrime(concat(ps[l],ps[j])) and \
                                IsPrime(concat(ps[k],ps[l])) and \
                                IsPrime(concat(ps[l],ps[k])):
                            for m in xrange(l+1, length):
                                if IsPrime(concat(ps[i],ps[m])) and \
                                        IsPrime(concat(ps[m],ps[i])) and \
                                        IsPrime(concat(ps[j],ps[m])) and \
                                        IsPrime(concat(ps[m],ps[j])) and \
                                        IsPrime(concat(ps[k],ps[m])) and \
                                        IsPrime(concat(ps[m],ps[k])) and \
                                        IsPrime(concat(ps[l],ps[m])) and \
                                        IsPrime(concat(ps[m],ps[l])):
                                    print ps[i],ps[j],ps[k],ps[l],ps[m]
                                    print '\t', sum([ps[i],ps[j],ps[k],ps[l],ps[m]])
                                    quit()
