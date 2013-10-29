def prime_numbers(limit=100000):
    '''Prime number generator. Yields the series
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29 ...
    using Sieve of Eratosthenes.
    '''
    yield 2
    sub_limit = int(limit**0.5)
    flags = [True, True] + [False] * (limit - 2)
    # Step through all the odd numbers
    for i in range(3, limit, 2):
        if flags[i]:
            continue
        yield i
        # Exclude further multiples of the current prime number
        if i <= sub_limit:
            for j in range(i*i, limit, i<<1):
                flags[j] = True

primes = list(prime_numbers(100000))

def is_prime(n):
    global primes
    for p in primes:
        if not n % p:
            return False
    return True

def main(n):
    s = 0
    for r1 in '123456789':
        for r2 in '123456789':
            if is_prime(int(r1+'00000000'+r2)):
                s += int(r1+'00000000'+r2)
    for d in '1345679':
        temp = s
        for pos in range(10):
            for r in '0123456789':
                if r == d or (r == '0' and pos == 0):
                    continue
                if is_prime(int( d*pos + r + d*(9-pos) )):
                    s += int( d*pos + r + d*(9-pos) )
        if temp == s:
            print d + ' did not have any!'
    for d in '28':
        temp = s
        for p1 in range(9):
            for p2 in range(p1+1,10):
                for r1 in '0123456789':
                    if (r1 == '0' and p1 == 0):
                        continue
                    for r2 in '0123456789':
                        if r2 == d:
                            continue
                        if is_prime(int( d*p1 + r1 + d*(p2-p1-1) + r2 + d*(9-p2))):
                            if r1 == d:
                                print d*p1 + r1 + d*(p2-p1-1) + r2 + d*(9-p2) 
                            s += int(d*p1 + r1 + d*(p2-p1-1) + r2 + d*(9-p2))
        if temp == s:
            print d + ' did not have any!'
                    
    return s
        
    
if __name__ == "__main__":
    print main(10)

    
        


