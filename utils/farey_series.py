def main(An,Ad,Bn,Bd,Dlim):
    stuff.append([float(An)/float(Ad),An,Ad])
    recurse(An,Ad,Bn,Bd,Dlim)
    stuff.append([float(Bn)/float(Bd),Bn,Bd])

def recurse(An,Ad,Bn,Bd,Dlim):
    if (Ad+Bd) > Dlim:
        return 0
    n = An + Bn
    d = Ad + Bd
    stuff.append([float(n)/float(d),n,d])
    lsum = recurse(An,Ad,n,d,Dlim)
    rsum = recurse(Bn,Bd,n,d,Dlim)
    return lsum + rsum + 1


main(249,499,1,2,600)
stuff = sorted(stuff)
for i in xrange(0,len(stuff)-1):
    print '  res += recurse(%d,%d,%d,%d,1000000);'%(stuff[i][1],stuff[i][2],stuff[i+1][1],stuff[i+1][2])
