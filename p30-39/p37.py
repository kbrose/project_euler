from array import *

n = 1000000 # finds primes up to n

sieve = [1]*n

sieve[0] = 0
sieve[1] = 0

for i in xrange(2, int(n ** 0.5) + 1):
    for j in xrange(i << 1, n, i):
        sieve[j] = 0


def testleft(n):
    while(n > 10):
        if not sieve[n]:
            return 0
        n = n / 10
    return sieve[n]

def testright(n):
    log = 1
    while(log <= n):
        log = log * 10
    log = log / 10
    while(n > 10):
        if not sieve[n]:
            return 0
        n = n - ((n / log)*log)
        log = log / 10
    return sieve[n]

counter = 0
i = 10
sum = 0

while(not counter == 11):
    if testleft(i) and testright(i):
        sum = sum + i
        counter = counter + 1
    i = i + 1

print sum
        
