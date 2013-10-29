def primes(N):
    sieve = [1]*N
    sieve[0] = 0
    sieve[1] = 0 # apparently 1 is not prime
    primes = [2]
    for i in xrange(4,N,2):
        sieve[i] = 0
    for i in xrange(3, int(N ** 0.5) + 1,2):
        if sieve[i]:
            primes.append(i)
            for j in xrange(i << 1, N, i):
                sieve[j] = 0
    # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # return sieve
    # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    start = int((int(N)**.5)+1)
    if not start % 2:
        start += 1
    for i in xrange(start,N,2):
        if sieve[i]:
            primes.append(i)
    return [sieve,primes]

N = 100000
storage = primes(N)
primes = storage[1]
sieve = storage[0]

def isPrime(n):
    if n >= N:
        end = n**.5 + 1
        i = 0
        while primes[i] < end:
            if not n % primes[i]:
                return 0
        return 1
    return sieve[n]

solved = 0
sols = [0]*12001
answers = set()
sols[2] = 4

def recurse(factors, start, end, original_n, new_n):
    if len(factors) > 13:
        return 0
    if isPrime(new_n):
        factors += [new_n]
        new_n = 1
    if new_n == 1:
        k = original_n - sum(factors) + len(factors)
        if k > 12000 or k < 2:
            return 0
        if sols[k] == 0:
            sols[k] = original_n
            return 1
        return 0
    s = 0
    for i in xrange(start, end):
        if not new_n % i:
            s += recurse(factors + [i], i, end, original_n, new_n / i)
    return s

def main():
    solved = 0
    n = 5
    while solved < 11998:
        solved += recurse([],2, (n / 2) + 1, n,n)
        n += 1
    for k in xrange(2,12001):
        answers.add(sols[k])
    return sum(answers)

print main()
