def MultOrd(a, n):
    k = 1
    while ((pow(a, k)-1) % n) > 0:
        k = k + 1
    return k

def period(n):
    # wikipedia says the 5 and 2 factors don't matter
    while((n % 5) == 0):
        n = n / 5
    while((n % 2) == 0):
        n = n / 2
    return MultOrd(10, n)

currlen = 0
currid = 0

for i in xrange(1,1000):
    templen = period(i)
    if(templen > currlen):
        currlen = templen
        currid = i

print currid
