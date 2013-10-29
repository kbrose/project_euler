from array import *

# sieve
# primes
# p_length = len(primes)

def main(N):
    N += 1
    sieve = [1]*N
    sieve[0] = 0
    sieve[1] = 0 # apparently 1 is not prime
    primes = [2]
    for i in xrange(4,N,2):
        sieve[i] = 0
    for i in xrange(3, int(N ** 0.5) + 1,2):
        if sieve[i]:
            primes.append(i)
            for j in xrange(i << 1, N, i):
                sieve[j] = 0
    start = int((int(N)**.5)+1)
    if not start % 2:
        start += 1
    for i in xrange(start,N,2):
        if sieve[i]:
            primes.append(i)
    p_length = len(primes)
    cond_p_factors = {}
    for n in xrange(2,N):
        if sieve[n]:
            cond_p_factors[n] = [n]
            continue
        for i in xrange(0,p_length):
            if n % primes[i] == 0:
                # if you don't want it condensed, comment out next three lines
                if primes[i] in cond_p_factors[n/primes[i]]:
                    cond_p_factors[n] = cond_p_factors[n/primes[i]]
                    break
                cond_p_factors[n] = sorted([primes[i]]+cond_p_factors[n/primes[i]])
                break
    cumulative_phi = 0
    for n in xrange(2,N):
        #if sieve[n]:
        #    cumulative_phi += n-1
        phi_n = n
        for p in cond_p_factors[n]:
            phi_n /= p
            phi_n *= (p-1)
        cumulative_phi += phi_n
    return cumulative_phi

print main(1000000)


