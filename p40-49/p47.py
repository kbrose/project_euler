from array import *

n = 1000000 # finds primes up to n

sieve = [1]*n

sieve[0] = 0
sieve[1] = 1

for i in xrange(2, int(n ** 0.5) + 1):
    for j in xrange(i << 1, n, i):
        sieve[j] = 0

def IsPrime(n):
    return sieve[n]

def PrimeFactors(n):
    i = -1
    factors = []
    p = 2
    while not sieve[n]:
        while not sieve[p]:
            p = p + 1
        if n % p == 0:
            n = n / p
            factors.append([p,1])
            i = i + 1
            while n % p == 0:
                n = n / p
                factors[i][1] = factors[i][1] + 1
        p = p + 1
    factors.append([n,1])
    return factors

def main():
    facts1 = PrimeFactors(644)
    facts2 = PrimeFactors(645)
    facts3 = PrimeFactors(646)
    facts4 = PrimeFactors(647)
    i = 648

    while 1:
        ok = 1
        for facts in facts1:
            if (facts in facts2) or (facts in facts3) or (facts in facts4):
                ok = 0
                break
        for facts in facts2:
            if (facts in facts3) or (facts in facts4):
                ok = 0
                break
        for facts in facts3:
            if (facts in facts4):
                ok = 0
                break
        if not len(facts1) == 4:
            ok = 0
        if not len(facts2) == 4:
            ok = 0
        if not len(facts3) == 4:
            ok = 0
        if not len(facts4) == 4:
            ok = 0
        if ok:
            return i - 4
        facts1 = facts2
        facts2 = facts3
        facts3 = facts4
        facts4 = PrimeFactors(i)
        i = i + 1

print main()
