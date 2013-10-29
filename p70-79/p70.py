from array import *
import time

def permutes(a,b):
    x = []
    i = 0
    while a > 0:
        x.append(a % 10)
        i += 1
        a /= 10
    y = []
    i = 0
    while b > 0:
        y.append(b % 10)
        i += 1
        b /= 10
    length = len(x)
    if not length == len(y):
        return 0
    for i in xrange(0,length):
        if x[i] in y:
            y[y.index(x[i])] = [-1]
        else:
            return 0
    return 1

def main(N):
    sieve = [1]*(N/2+1)
    sieve[0] = 0
    sieve[1] = 0 # apparently 1 is not prime
    primes = [2]
    for i in xrange(4,(N/2)+1,2):
        sieve[i] = 0
    for i in xrange(3, int((N/2+1) ** 0.5) + 1,2):
        if sieve[i]:
            primes.append(i)
            for j in xrange(i << 1, (N/2)+1, i):
                sieve[j] = 0
    start = int((int((N/2)+1)**.5)+1)
    if not start % 2:
        start += 1
    for i in xrange(start,N/2+1,2):
        if sieve[i]:
            primes.append(i)
    i = 0
    while primes[i]*primes[i+1] < N:
        i += 1
    i -= 1
    pMin = i
    upper = i+1
    for lower in range(pMin,-1,-1):
        while primes[lower]*primes[upper] < N:
            upper += 1
        upper -= 1
        for pMax in range(upper,pMin,-1):
            pl = (primes[lower])
            pu = (primes[pMax])
            phi = (pl-1)*(pu-1)
            if permutes(phi,pl*pu):
                return pl*pu
    return -1
    
print main(100000000)
quit()
    

def main(N):
    sieve = [1]*N
    sieve[0] = 0
    sieve[1] = 0 # apparently 1 is not prime
    primes = []
    p_facts = {}
    for i in xrange(2, int(N ** 0.5) + 1):
        if sieve[i]:
            primes.append(i)
            for j in xrange(i << 1, N, i):
                sieve[j] = 0
    for i in xrange(2,N):
        p_facts[i] = [1]
    for p in primes:
        for i in xrange(p, N, p):
                p_facts[i] += [p]
    phi = [-1,-1]
    curr_min = 10000000
    for i in xrange(2,N):
        if sieve[i]:
            continue
        p = i
        if len(p_facts[i]) > 1:
            for j in xrange(1,len(p_facts[i])):
                p *= (1 - 1.0/p_facts[i][j])
        if permutes(i,p):
            if float(i)/p < curr_min:
                curr_min = float(i)/p
                curr_n = i
    return curr_n

#print main(10000000)
