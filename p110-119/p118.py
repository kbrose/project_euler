from itertools import permutations
from itertools import combinations

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

primes = list(prime_numbers(31428*2))

def is_prime(n):
    if n == 1:
        return False
    global primes
    sq_n = int(n**0.5)
    for p in primes:
        if p > sq_n:
            break
        if not n % p:
            return False
    return True
    
def get_int(c):
    ret = ''
    for num in c:
        ret += num
    return int(ret)

def get_used(n):
    used = [1] + [0]*9
    while n > 0:
        used[n % 10] = 1
        n /= 10
    return tuple(used)

def join_used(a,b):
    used = [1] + [0]*9
    for i in range(10):
        used[i] = a[i] or b[i]
    return tuple(used)

def set_no_reps(s, p):
    used = list(s)
    while p > 0:
        if used[p % 10]:
            return False
        p /= 10
    return True

    
primes = list(prime_numbers(31428))

possibles = {}
possibles_update = {}
all_sets = {}

for length in range(9,0,-1):
    for c in permutations('123456789', length):
        p = get_int(c)
        if is_prime(p):
            possibles_update = {}
            for used in possibles:
                if set_no_reps(used,p):
                    joined = join_used(used, get_used(p))
                    if joined in possibles:
                        possibles[joined] += possibles[used]
                    else:
                        possibles_update[joined] = possibles[used]
            if get_used(p) in possibles:
                possibles[get_used(p)] += 1
            else:
                possibles[get_used(p)] = 1
            possibles.update(possibles_update)
            del(possibles_update)

# print len(possibles)
print possibles[(1,1,1,1,1,1,1,1,1,1)]

    
