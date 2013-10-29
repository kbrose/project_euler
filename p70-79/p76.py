def main(N):
    P = {-1:0,0:1,1:1}
    for n in xrange(2,N+1):
        s = 0
        mult = 1
        for k in xrange(1,n+1):
            p1 = n-((k*(3*k-1))/2)
            p2 = n-((k*(3*k+1))/2)
            p1neg = 0
            if p1 < 0:
                p1 = -1
                p1neg = 1
            if p2 < 0:
                if p1neg:
                    break
                p2 = -1
            s += mult * (P[p1] + P[p2])
            mult *= -1
        P[n] = s
    return P

N = 100
print main(N)[N]-1
