from array import *
import itertools

n = 1000000 # finds primes up to n

sieve = [1]*n

sieve[0] = 0
sieve[1] = 0 # apparently 1 is not prime

for i in xrange(2, int(n ** 0.5) + 1):
    for j in xrange(i << 1, n, i):
        sieve[j] = 0

def IsPrime(n):
    return sieve[n]

# populated only with primes > 99999 
primes = []
for i in xrange(99999,1000000):
    if IsPrime(i):
        primes.append(i)

def arrToNumBackwards(array):
    if array[len(array)-1] == 0:
        return 0
    num = array[0]
    multiplier = 10
    for i in xrange(1,len(array)):
        num = num + array[i]*multiplier
        multiplier *= 10
    return num

def numToArrBackwards(n):
    arr = []
    while(n > 0):
        arr.append(n % 10)
        n /= 10
    return arr

replace1of6 = list(itertools.combinations([0,1,2,3,4,5],1))
replace2of6 = list(itertools.combinations([0,1,2,3,4,5],2))
replace3of6 = list(itertools.combinations([0,1,2,3,4,5],3))
replace4of6 = list(itertools.combinations([0,1,2,3,4,5],4))
replace5of6 = list(itertools.combinations([0,1,2,3,4,5],5))

def test(n, p):
    if n == 1:
        rep = replace1of6
    if n == 2:
        rep = replace2of6
    if n == 3:
        rep = replace3of6
    if n == 4:
        rep = replace4of6
    if n == 5:
        rep = replace5of6
    maxx = 0
    for perm in rep:
        count = 0
        reps = list(perm)
        backarr = numToArrBackwards(p)
        for x in xrange(0,10):
            temp = backarr

            checker = temp[reps[0]]
            for i in reps:
                if not temp[i] == checker:
                    checker = -1
            if checker == -1:
                break

            for i in reps:
                temp[i] = x
            if IsPrime(arrToNumBackwards(temp)):
                count += 1
        if count > maxx:
            maxx = count
    return maxx

for p in primes:
    if test(1,p) > 7:
        print p
        break
    if test(2,p) > 7:
        print p
        break
    if test(3,p) > 7:
        print p
        break
    if test(4,p) > 7:
        print p
        break
    if test(5,p) > 7:
        print p
        break
