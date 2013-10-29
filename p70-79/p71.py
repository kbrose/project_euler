def main(a,b,lim):
    res = [1,lim]
    for d in xrange(b,lim+1):
        n = (a*d-1)/b
        if res[0]*d < res[1]*n:
            res[0] = n
            res[1] = d
    return res

print main(5,11,1000000)
