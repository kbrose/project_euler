f = [1,1,2,6,24,120,720,5040,40320,362880]

def f_digs(n):
    s = 0
    while n > 0:
        s += f[n % 10]
        n /= 10
    return s

counter = 0
for n in xrange(2,1000000):
    non_repeats = 0
    arr = []
    while not n in arr:
        arr.append(n)
        n = f_digs(n)
        non_repeats += 1
        if non_repeats > 60:
            non_repeats = 0
            break
    if non_repeats == 60:
        counter += 1

print counter
