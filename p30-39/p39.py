currmaxsol = 0

for p in xrange(12,1000):
    sols = 0
    for a in xrange(1,p-1):
        for b in xrange(a,p-1):
            experimentalp = ((a*a + b*b)**.5) + a + b
            if experimentalp > p:
                break
            if p == experimentalp:
                sols = sols + 1
    if sols > currmaxsol:
        currmaxsol = sols
        currmaxper = p

print currmaxper, currmaxsol
