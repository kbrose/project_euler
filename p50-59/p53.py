f = [1]*101
for i in xrange(1,101):
    f[i] = f[i-1]*i

def odd_routine(n):
    for r in xrange(0, (n/2)+1):
        if f[n] / (f[r] * f[n-r]) > 1000000:
            return (((n / 2) + 1) - r) * 2
    return 0

def even_routine(n):
    for r in xrange(0, (n/2)+1):
        if f[n] / (f[r] * f[n-r]) > 1000000:
            return ((n / 2) - r) * 2 + 1
    return 0

n = 1
count = 0

while n < 101:
    count += odd_routine(n)
    count += even_routine(n+1)
    n += 2

print count
