from array import *
from primes import *

def main(N,M):
    b = [1,0,1]
    c = [0,1,1]
    n = 2
    p_facts = p_factors_cond(N)
    while b[n] <= M:
        n += 1
        c.append(sum(p_facts[n]))
        s = 0
        for k in xrange(1,n):
            s += c[k] * b[n-k]
        s += (c[n])
        s /= n
        b.append(s)
    return n


print main(10000,10000)
