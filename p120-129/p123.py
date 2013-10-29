import primes

# same logic as p120
# I was hoping since these were primes that
# maybe Fermat's Little Theorem would show up
# ... but it didn't.

def check(p,n,target):
    return 2*p*n > target

def main():
    ps = primes.primes(250000)
    i = 0
    while not check(ps[i],i+1,10**10):
        i += 2
    print i+1 # zero indexing, yo

main()
