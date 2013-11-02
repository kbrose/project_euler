# much like the sieve of Eratosthenes, this will go through all
# the numbers 1...limit, increasing their rad value as necessary
# then it will sort based on criterion

def E(k,limit):
    rads = [[1,i] for i in range(limit)]
    for i in range(2,limit):
        if rads[i][0] == 1: # is a prime, commence sieve
            for j in range(i, limit, i):
                rads[j][0] *= i
    return (sorted (rads))[k-1][1]

print E(10000,100000)
