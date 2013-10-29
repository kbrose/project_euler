from itertools import permutations
from array import *

n = 10000 # finds primes up to n

p = [1]*n

p[0] = 0
p[1] = 1

for i in xrange(2, int(n ** 0.5) + 1):
    for j in xrange(i << 1, n, i):
        p[j] = 0

def main():
    for a in xrange(1,10):
        for b in xrange(1,10):
            for c in xrange(1,10):
                for d in xrange(1,10):
                    l = list(permutations([a,b,c,d],4))
                    for first in l:
                        firstn = first[0]*1000 + first[1]*100 + first[2]*10 + first[3]
                        for sec in l:
                            secn = sec[0]*1000 + sec[1]*100 + sec[2]*10 + sec[3]
                            for third in l:
                                thirdn=third[0]*1000+third[1]*100+third[2]*10+third[3]
                                ok = 1
                                if not thirdn - 3330 == secn:
                                    ok = 0
                                if not secn - 3330 == firstn:
                                    ok = 0
                                if not (p[firstn] and p[secn] and p[thirdn]):
                                    ok = 0
                                if ok:
                                    if firstn == 1487:
                                        break
                                    print firstn,secn,thirdn
                                    return

main()
