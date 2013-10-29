from array import *

n = 100000 

sieve = [1]*n

sieve[0] = 0
sieve[1] = 1

for i in xrange(2, int(n ** 0.5) + 1): 
    for j in xrange(i << 1, n, i):
        sieve[j] = 0

squares = dict.fromkeys((x*x for x in xrange(1, 100)), 1)


def main():
    for i in xrange(3,100000,2):
        #print i
        if not sieve[i]:
            ok = 1
            for prime in xrange(1,i):
                if not sieve[prime]:
                    continue
                if ((i - prime)/2) in squares:
                    ok = 0
                    break
            if ok:
                print i
                return

main()
