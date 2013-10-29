import math

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

def prod(l):
    ret = 1
    for item in l:
        ret *= item[0]**item[1]
    return ret

def sols(factors):
    ret = 1
    for factor in factors:
        ret *= (2*factor[1] + 1)
    return (ret + 1) / 2

def prime_factorization(n, primes):
    i = 0
    ret = []
    while n > 1:
        if not n % primes[i]:
            ret.append([primes[i],0])
        while not n % primes[i]:
            n /= primes[i]
            ret[len(ret)-1][1] += 1
        i += 1
    return ret

def prime_factorizations(N, primes):
    'Returns the prime factorization of numbers up to (but not) N'
    ret = []
    if N < 2:
        return ret
    for i in range(2,N):
        ret.append(prime_factorization(i, primes))
    return ret
    
def get_new_list(l):
    ret = []
    for item in l:
        ret.append(list(item))
    return ret

def concatenate_p_factors(l1, l2):
    for item_2 in l2:
        for item_1 in l1:
            if item_2[0] == item_1[0]:
                item_1[1] += item_2[1]

def unconcatenate_p_factors(l1, l2):
    for item_2 in l2:
        for item_1 in l1:
            if item_2[0] == item_1[0]:
                item_1[1] -= item_2[1]

def main(N):
    primes = list(prime_numbers(10000))
    factors = []
    n = 1
    while 3**n < 2*N:
        n += 1
    for i in range(n):
        factors.append([primes[i],1])
        
    factors.reverse()
    
    for f in factors:
        if f[1] > 1:
            break
        if f[1] == 0:
            continue
        new_factors = get_new_list(factors)
        new_factors[new_factors.index(f)] = [f[0],0]
        changed = False
        for p_fact in prime_factorizations(f[0], primes):
            concatenate_p_factors(new_factors, p_fact)
            if sols(new_factors) > N:
                changed = True
                break
            unconcatenate_p_factors(new_factors, p_fact)
        if changed:
            factors = get_new_list(new_factors)
        if not changed:
            break
           
    return prod(factors)

if __name__ == "__main__":
    print main(1*(10**3))
        

# print main(180180) # = 1013, 180180 = 2*2*5*3*3*7*11*13
